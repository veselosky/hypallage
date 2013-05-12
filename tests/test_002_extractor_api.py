"""
Tests for hypallage use the pytest framework.

This test case exercises the Extractor API.
"""
import pytest
import os.path as path
here = path.dirname(__file__)


@pytest.fixture(scope="module")
def doc():
    articlefile = path.join(here, 'data', 'schema.org', 'Article.microdata')
    from hypallage.microdata import Extractor
    doc = Extractor(articlefile)
    return doc


def test_00_items(doc):
    assert len(doc.items) > 0


def test_01_document(doc):
    import bs4
    assert isinstance(doc.document, bs4.BeautifulSoup)


def test_02_to_json(doc):
    # NOTE Our Extractor sorts keys by default to make the output string
    # comparable. This is NOT required by SPEC.
    assert doc.to_json() == '{"items":[{"properties":{"author":["John Doe"],"interactionCount":["UserTweets:1203","UserComments:78"],"name":["How to Tie a Reef Knot"]},"type":"http://schema.org/Article"}]}'  # noqa


def test_03_to_json_pretty(doc):
    # Sorry pep8, trailing whitespace is expected in this string. Grrr.
    assert doc.to_json(indent=2) == """{
  "items": [
    {
      "properties": {
        "author": [
          "John Doe"
        ], 
        "interactionCount": [
          "UserTweets:1203", 
          "UserComments:78"
        ], 
        "name": [
          "How to Tie a Reef Knot"
        ]
      }, 
      "type": "http://schema.org/Article"
    }
  ]
}"""
