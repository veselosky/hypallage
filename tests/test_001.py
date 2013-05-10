"""
Tests for hypallage use the pytest framework.

This test case tests handing the Extractor a pre-parsed BeautifulSoup tree.
"""
#import pytest
import os.path as path
here = path.dirname(__file__)


def test_00_construction_from_bs4():
    articlefile = path.join(here, 'data', 'schema.org', 'Article.microdata')
    import bs4
    html = bs4.BeautifulSoup(open(articlefile))
    from hypallage.microdata import Extractor
    doc = Extractor(html)
    assert doc.items[0]['type'] == 'http://schema.org/Article'


def test_01_soup_accessor():
    articlefile = path.join(here, 'data', 'schema.org', 'Article.microdata')
    import bs4
    html = bs4.BeautifulSoup(open(articlefile))
    from hypallage.microdata import Extractor
    doc = Extractor(html)
    assert isinstance(doc.document, bs4.BeautifulSoup)
    assert doc.document is html

