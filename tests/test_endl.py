import os
import sys

from cppstream import cout as _real_cout
from cppstream import endl


def get_cout():
    # need to dynamically replace the stream to the sys.stdout from this module
    # rather than the preset one otherwise the test will fail
    # see pull #2
    # also pytest-dev/pytest#9916
    _real_cout._stream = sys.stdout
    return _real_cout


def test_endl_writes_newline(capsys):
    cout = get_cout()
    cout << "Hello"
    cout << endl
    cout << "World"
    cout << endl

    cap = capsys.readouterr()
    assert cap.out == f"Hello{os.linesep}World{os.linesep}"
