"""
Hypallage util contains classes and functions for general use by other
hypallage libraries.
"""
try:  # python 3
    import urllib.parse as urlparse
except ImportError:  # python 2
    import urlparse


class URI(str):
    """
    Representation of a URI, based on RFC3986. Pass a string to the
    constructor to initialize it.
    """

    def __init__(self, uristr='', base=''):
        super(URI, self).__init__(uristr)
        self.original_uri = uristr
        self.parsed_url = urlparse.urlparse(uristr)
        self.parsed_base = urlparse.urlparse(base)

        self.scheme = self.parsed_url.scheme or self.parsed_base.scheme
        self.netloc = self.parsed_url.netloc or self.parsed_base.netloc
        self.path = self.parsed_url.path or self.parsed_base.path
        self.params = self.parsed_url.params or self.parsed_base.params
        self.query = self.parsed_url.query or self.parsed_base.query
        self.fragment = self.parsed_url.fragment or self.parsed_base.fragment
        self.username = self.parsed_url.username or self.parsed_base.username
        self.password = self.parsed_url.password or self.parsed_base.password
        self.hostname = self.parsed_url.hostname or self.parsed_base.hostname
        self.port = self.parsed_url.port or self.parsed_base.port

        # TODO Resolution per RFC3986 Section 5.

    def normalized(self):
        return urlparse.urlunparse([self.scheme,
                                    self.netloc,
                                    self.path,
                                    self.params,
                                    self.query,
                                    self.fragment])

    def __str__(self):
        return self.normalized()

    def __eq__(self, other):
        if isinstance(other, URI):
            return self.normalized() == other.normalized()
        else:  # assume string
            # TODO Equivalence comparison per RFC3986 6.2.2, 6.2.3
            return self.normalized() == URI(other).normalized()


def to_json(o):
    """
    Function for passing as the `default` argument to `json.dump`.

    This conversion function knows how to handle several problematic types
    used in hypallage.
    """
    if isinstance(o, URI):
        return o.normalized()
    else:
        raise TypeError


def str_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None


def str_to_uri(value):
    return URI(value)


schema_convert = {'Integer': str_to_int, 'URI': str_to_uri}

