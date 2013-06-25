"""
.. module hypallage.microdata

Microdata
==========

This module contains tools for working with HTML 5 microdata.
"""
# NOTE The SPEC for HTML5 microdata lives at
# http://www.whatwg.org/specs/web-apps/current-work/multipage/microdata.html
# To resolve URLs in comments below, substitute this URL for SPEC.

import bs4
from bs4 import BeautifulSoup as bs
import os.path as path
try:  # python 3
    from urllib.request import urlopen
except ImportError:  # python 2
    from urllib2 import urlopen

from hypallage import util


class Extractor(object):
    """
    :param extract_from: file path, URL, or BeautifulSoup instance.

    HTML 5 microdata extractor.
    """

    def __init__(self, extract_from):
        self._items = None
        if isinstance(extract_from, bs4.BeautifulSoup):
            self.document = extract_from

        elif path.exists(extract_from):
            with open(extract_from) as thefile:
                rawhtml = thefile.read()
            self.document = bs(rawhtml)

        else:
            with urlopen(extract_from) as thefile:
                rawhtml = thefile.read()
            self.document = bs(rawhtml)

    value_attr = \
        {
            'meta': 'content',
            'audio': 'src',
            'embed': 'src',
            'iframe': 'src',
            'img': 'src',
            'source': 'src',
            'track': 'src',
            'video': 'src',
            'a': 'href',
            'area': 'href',
            'link': 'href',
            'object': 'data',
            'data': 'value',
            'time': 'datetime',
        }

    @property
    def items(self):
        """
        A list of the extracted items.
        """
        if self._items is None:
            self._items = self._extract_items()
        return self._items

    def to_json(self, **kwargs):
        """
        :returns: a serialized JSON string.
        :param kwargs: any key-word arguments accepted by :py:func:`json.dumps`

        By default, behaves according to the HTML5 specification, returning
        the most compact form possible. To ease string comparisons, also
        returns the keys sorted. You can override these defaults by passing
        kwargs.
        """
        import json
        # To be compliant with SPEC#extracting-json, we must have no whitespace
        # between tokens by default. The default json separator includes
        # spaces, so we need to replace them. But the caller can override this
        # if they don't care about the spec.
        if 'separators' not in kwargs and 'indent' not in kwargs:
            kwargs['separators'] = (',', ':')

        # To ease comparisons, sort the keys by default. My reading of
        # SPEC#extracting-json allows this, as order of properties is not
        # specified.
        if 'sort_keys' not in kwargs:
            kwargs['sort_keys'] = True

        # TODO Use our own JSONEncoder that knows how to deal with URLs and
        # the various datetime types.
        return json.dumps({'items': self.items},
                          default=util.to_json,
                          **kwargs)

    def is_itemscope(self, node):
        return node.get('itemscope') is not None

    def is_itemprop(self, node):
        return node.get('itemprop') is not None

    # See SPEC#extracting-json
    def _extract_items(self):
        itemnodes = self.document.find_all(itemscope=True, itemprop=False)
        if not itemnodes:
            return []
        items = []
        for node in itemnodes:
            items.append(self._extract_item(node))
        return items

    # See SPEC#get-the-object
    def _extract_item(self, itemnode, memory=[]):
        memory.append(itemnode)
        item = {}
        if itemnode.get('itemtype'):
            item['type'] = util.URI(itemnode.get('itemtype'))
        if itemnode.get('itemid'):
            item['id'] = itemnode.get('itemid')
        item['properties'] = self._extract_properties(itemnode,
                                                      memory,
                                                      item.get('type'))
        return item

    def _extract_properties(self, itemnode, memory, itemtype=None):
        # NOTE: results are supposed to be sorted in tree order. If no itemref
        # exists to muddy the waters, a depth-first traversal accomplishes
        # this.  When there is an itemref, order cannot be assured, and the
        # results must be sorted. Since the sort is ambiguous, we have to
        # return a list rather than an iterator.
        nodelist = []
        for child in itemnode.children:
            nodelist.extend(self._extract_propertynodes(child, memory))
        if itemnode.get('itemref'):
            for ref in itemnode.get('itemref'):
                node = self.document.find(id=ref)
                nodelist.extend(self._extract_propertynodes(node, memory))
            # TODO SORT nodelist HERE

        # NOTE Property values are always stored as arrays, per SPEC#json
        properties = {}
        for node in nodelist:
            props = node['itemprop'].split()
            for prop in props:
                if prop not in properties:
                    properties[prop] = []
                properties[prop].extend(
                    self._extract_property_value(node, itemtype))
        return properties

    # See SPEC#the-properties-of-an-item
    def _extract_propertynodes(self, node, memory=[]):
        propertynodes = []
        # If it's not a tag, it's not a propertynode
        if not isinstance(node, bs4.Tag):
            return propertynodes

        if node.get('itemprop'):  # present AND not empty
            propertynodes.append(node)

        # DO NOT DESCEND into another itemscope
        if self.is_itemscope(node):
            return propertynodes

        for child in node.children:
            if child in memory:  # Error, circular reference. Skip.
                # TODO Log this error for user feedback
                # FIXME SPEC#get-the-object @7.2 says this should generate
                # the string "ERROR", but this is problematic.
                continue
            memory.append(child)
            propertynodes.extend(self._extract_propertynodes(child, memory))
        return propertynodes

    # See SPEC#concept-property-value
    def _extract_property_value(self, node, itemtype=None):
        # If the node is an item, the value is the extracted item.
        if self.is_itemscope(node):
            value = self._extract_item(node)
            # print("Found sub-item %s" % value)
            return [value]

        # Normally the value is an attribute of the node, as defined in SPEC
        elif node.name in self.value_attr:
            value = node[self.value_attr[node.name]]

        # If none of that works, SPEC says extract the text
        else:
            value = node.get_text()

        # Now translate to the correct data type.
        value_type = self._detect_type(node, itemtype)
        # print("Detected type %s for value %s" % (value_type, value))
        value = self.to_python_type(value, value_type)

        # NOTE Property values are always stored as arrays, per SPEC#json
        return [value]

    def _detect_type(self, node, itemtype=None):
        # These attributes are required to be URIs:
        detected_type = None
        if node.name in self.value_attr \
                and self.value_attr[node.name] in ['src', 'href']:
            detected_type = [util.URI('URI')]

        # time elements always represent a datetime
        elif node.name == 'time':
            detected_type = [util.URI('DateTime'),
                             util.URI('Date'),
                             util.URI('Time')]

        # If the itemtype is defined by schema.org, lookup the specified
        # type for the property.
        elif itemtype and itemtype.startswith('http://schema.org/'):
            from hypallage.schema import schema
            schema_prop = schema['properties'].get(node.get('itemprop'))
            if schema_prop and 'ranges' in schema_prop:
                detected_type = [util.URI(x) for x in schema_prop['ranges']]

        elif 'data-type' in node:
            detected_type = [node['data-type']]  # only one supported for now

        return detected_type

    def to_python_type(self, value, value_type):
        # value_type is a list of possible types. Attempt conversion in order.
        if not value_type:
            return value

        new_value = None

        for possible_type in value_type:
            # FIXME This is sloppy, but for now assume base is schema.org
            if possible_type.path in util.schema_convert:
                new_value = util.schema_convert[possible_type.path](value)
            if new_value:
                break

        return new_value or value

