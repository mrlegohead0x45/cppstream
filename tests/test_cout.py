import re
import sys

from pytest import raises

from cppstream import OutStream
from cppstream import cout as _real_cout


def get_cout():
    # need to dynamically replace the stream to the sys.stdout from this module
    # rather than the preset one otherwise the test will fail
    # see pull #2
    # also pytest-dev/pytest#9916
    _real_cout._stream = sys.stdout
    return _real_cout


def test_cout_basic(capsys):
    cout = get_cout()

    cout << "Hello World!"
    cout << 5
    cout << 5.5
    cout << True
    cout << None

    cap = capsys.readouterr()
    assert cap.out == "Hello World!55.5TrueNone"


def test_cout_custom_class(capsys):
    class MyClass:
        _iostream_streamable_from = True

        def _iostream_stream_from(self, ostream: OutStream):
            ostream << "MyClass"

    cout = get_cout()
    cout << MyClass()

    cap = capsys.readouterr()
    assert cap.out == "MyClass"


def test_cout_custom_class_no_streamable(capsys):
    class MyClass:
        pass

    cout = get_cout()
    cout << MyClass()

    cap = capsys.readouterr()
    # e.g <test_cout.test_cout_custom_class_no_streamable.<locals>.MyClass object at 0x00000282D0AACEB0>
    assert re.match(r"<[\w<>\.]+ object at 0x[\da-fA-F]+>", cap.out) is not None


def test_cout_custom_class_streamable_no_stream_from():
    class MyClass:
        _iostream_streamable_from = True

    cout = get_cout()
    with raises(AttributeError):
        cout << MyClass()


def test_cout_custom_class_str(capsys):
    class MyClass:
        def __str__(self):
            return "MyClass"

    cout = get_cout()
    cout << MyClass()

    cap = capsys.readouterr()
    assert cap.out == "MyClass"
