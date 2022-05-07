import sys

import pytest

from cppstream import cout as _real_cout


@pytest.fixture
def cout():
    _real_cout._stream = sys.stdout
    return _real_cout


def test_cout(cout, capsys):
    # with(capfd).disabled():
    # cout._stream = sys.stdout
    cout << "Hello World!"

    # cout.stream.flush()
    # print("Hello World!")
    # with capfd.disabled():
    # print(cout.stream is sys.stdout) # False
    cap = capsys.readouterr()
    assert cap.out == "Hello World!"


def test_cout_stream_replace(capsys):
    _real_cout._stream = sys.stdout

    _real_cout << "Hello World!"

    cap = capsys.readouterr()
    assert cap.out == "Hello World!"
