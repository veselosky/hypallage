"""
Hypallage util contains classes and functions for general use by other
hypallage libraries.
"""
try:  # python 3
    import urllib.parse as urlparse
except ImportError:  # python 2
    import urlparse


class URI(object):
    """
    Representation of a URI, based on RFC3986. Pass a string to the
    constructor to initialize it.
    """

    def __init__(self, uristr=''):
        self.original_uri = uristr
        self.parsed_url = urlparse.urlparse(uristr)

        self.scheme = self.parsed_url.scheme
        self.netloc = self.parsed_url.netloc
        self.path = self.parsed_url.path
        self.params = self.parsed_url.params
        self.query = self.parsed_url.query
        self.fragment = self.parsed_url.fragment
        self.username = self.parsed_url.username
        self.password = self.parsed_url.password
        self.hostname = self.parsed_url.hostname
        self.port = self.parsed_url.port

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

