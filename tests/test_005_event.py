"""
Tests for hypallage use the pytest framework.
"""
import pytest
import os.path as path
here = path.dirname(__file__)


@pytest.fixture(scope="module")
def doc():
    articlefile = path.join(here, 'data', 'schema.org',
                            'Event.microdata')
    from hypallage.microdata import Extractor
    doc = Extractor(articlefile)
    return doc


def test_00_type(doc):
    article = doc.items[0]
    assert article['type'] == 'http://schema.org/Event'


def test_01_id(doc):
    article = doc.items[0]
    assert 'id' not in article


def test_02a_location_type(doc):
    article = doc.items[0]
    location = article['properties']['location'][0]
    assert location["type"] == "http://schema.org/Place"


def test_02b_location_url(doc):
    article = doc.items[0]
    import hypallage.util as util
    location = article['properties']['location'][0]
    url = location["properties"]["url"][0]
    assert isinstance(url, util.URI)
    assert url.path == "wells-fargo-center.html"


def test_02c_location_address(doc):
    article = doc.items[0]
    address = article['properties']['location'][0]["properties"]["address"][0]
    assert address["type"] == 'http://schema.org/PostalAddress'
    assert address["properties"]["addressLocality"] == ["Philadelphia"]
    assert address["properties"]["addressRegion"] == ["PA"]


def test_03_offers(doc):
    article = doc.items[0]
    offer = article['properties']['offers'][0]
    assert offer["type"] == "http://schema.org/AggregateOffer"
    assert offer["properties"]["lowPrice"] == ["$35"]
    assert offer["properties"]["offerCount"] == [1934]


def test_04_startdate(doc):
    """
    Datetime properties should translate to datetime type.
    """
    article = doc.items[0]
    from datetime import datetime
    start = datetime(2011, 4, 21, 20)
    startDate = article['properties']['startDate'][0]
    assert startDate.isoformat() == start.isoformat()
    # <meta itemprop="startDate" content="2011-04-21T20:00">


def test_05_json(doc):
    correct = """{"items":[{"properties":{},"type":"http://schema.org/CreativeWork"}]}"""  # noqa
    assert doc.to_json() == correct

