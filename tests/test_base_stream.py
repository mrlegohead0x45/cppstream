from os import linesep

from pytest import raises

from cppstream import Stream


def test_base_stream_linesep():
    stream = Stream()
    assert stream.linesep == linesep


def test_base_stream_has_no_stream():
    stream = Stream()
    with raises(AttributeError):
        stream.stream
