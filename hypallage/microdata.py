"""
.. module hypallage.microdata
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


class Extractor(object):
    """HTML 5 microdata extractor"""

    def __init__(self, extract_from):
        """Constructor takes a file path or URL"""
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

    @property
    def items(self):
        if self._items is None:
            self._items = self._extract_items()
        return self._items

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
            item['type'] = itemnode.get('itemtype')
        if itemnode.get('itemid'):
            item['id'] = itemnode.get('itemid')
        item['properties'] = self._extract_properties(itemnode, memory)
        return item

    def _extract_properties(self, itemnode, memory):
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
                properties[prop].extend(self._extract_property_value(node))
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
    def _extract_property_value(self, node):
        # FIXME URLs are supposed to be resolved (relative to base, etc)
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
        if self.is_itemscope(node):
            value = self._extract_item(node)
        elif node.name in value_attr:
            value = node[value_attr[node.name]]
            if value_attr[node.name] in ['src', 'href']:
                # TODO Resolve URL properly here
                pass
        else:
            value = node.get_text()
        # NOTE Property values are always stored as arrays, per SPEC#json
        return [value]
