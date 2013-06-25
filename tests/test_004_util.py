"""
Tests for hypallage use the pytest framework.

This test case exercises the hypallage.util functions and classes.
"""
from hypallage import util


def test_00_empty_uri():
    uri = util.URI()
    assert isinstance(uri, util.URI)
    assert uri == ''
    assert uri == util.URI()  # Two empties should compare equivalent
    assert uri == util.URI('')  # Two empties should compare equivalent


def test_01_relative_uri_no_base():
    uri = util.URI('filename.html')
    assert isinstance(uri, util.URI)
    assert uri == 'filename.html'
    assert uri == util.URI('filename.html')
    assert uri.path == 'filename.html'


def test_02_str_to_uri():
    uri = util.schema_convert['URI']('filename.html')
    assert isinstance(uri, util.URI)
    assert uri == 'filename.html'
    assert uri == util.URI('filename.html')

