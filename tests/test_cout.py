import sys

from cppstream import cout as _real_cout


def get_cout():
    _real_cout._stream = sys.stdout
    return _real_cout


def test_cout_basic(capsys):
    cout = get_cout()

    cout << "Hello World!"
    cout << 5

    cap = capsys.readouterr()
    assert cap.out == "Hello World!5"
