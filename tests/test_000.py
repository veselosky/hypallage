"""
Tests for hypallage use the pytest framework.
"""
import pytest
import os.path as path
here = path.dirname(__file__)


@pytest.fixture(scope="module")
def article():
    articlefile = path.join(here, 'data', 'schema.org', 'Article.microdata')
    from hypallage.microdata import Extractor
    doc = Extractor(articlefile)
    return doc.items[0]


def test_00_type(article):
    assert article['type'] == 'http://schema.org/Article'


def test_01_id(article):
    assert 'id' not in article


def test_02_author(article):
    assert article['properties']['author'] == ['John Doe']


def test_03_name(article):
    assert article['properties']['name'] == ['How to Tie a Reef Knot']


def test_04_interactions(article):
    """
    Properties set multiple times must be an array with values in document
    order.
    """
    assert article['properties']['interactionCount'] == ['UserTweets:1203',
                                                         'UserComments:78']

