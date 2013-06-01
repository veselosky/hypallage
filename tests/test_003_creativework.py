"""
Tests for hypallage use the pytest framework.
"""
import pytest
import os.path as path
here = path.dirname(__file__)


@pytest.fixture(scope="module")
def doc():
    articlefile = path.join(here, 'data', 'schema.org',
                            'CreativeWork.microdata')
    from hypallage.microdata import Extractor
    doc = Extractor(articlefile)
    return doc


def test_00_type(doc):
    article = doc.items[0]
    assert article['type'] == 'http://schema.org/CreativeWork'


def test_01_id(doc):
    article = doc.items[0]
    assert 'id' not in article


def test_02_author(doc):
    article = doc.items[0]
    assert article['properties']['author'] == ['Sony']


def test_03_name(doc):
    article = doc.items[0]
    assert article['properties']['name'] == ['Resistance 3: Fall of Man']


def test_04_rating(doc):
    """
    Properties set multiple times must be an array with values in document
    order.
    """
    article = doc.items[0]
    # FIXME: What does SPEC say about case normalizaiton?
    assert article['properties']['contentRating'] == ['Mature']


def test_05_image_str(doc):
    # Image is a URL. The URL object should be comfortable masquerading as a
    # string.
    article = doc.items[0]
    assert article['properties']['image'][0] == "videogame.jpg"


def test_06_image_url(doc):
    article = doc.items[0]
    import hypallage.util as util
    img = article['properties']['image'][0]
    assert isinstance(img, util.URI)
    assert img.path == 'videogame.jpg'


def test_07_json(doc):
    correct = """{"items":[{"properties":{"author":["Sony"],"contentRating":["Mature"],"image":["videogame.jpg"],"name":["Resistance 3: Fall of Man"]},"type":"http://schema.org/CreativeWork"}]}"""  # noqa
    assert doc.to_json() == correct

