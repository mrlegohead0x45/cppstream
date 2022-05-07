import sys

from cppstream import cout


def test_cout(capfd):
    # with(capfd).disabled():
    # cout._stream = sys.stdout
    cout << "Hello World!"

    # cout.stream.flush()
    # print("Hello World!")
    # with capfd.disabled():
    # print(cout.stream is sys.stdout) # False
    cap = capfd.readouterr()
    assert cap.out == "Hello World!"
