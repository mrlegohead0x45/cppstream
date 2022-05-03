from cppstream import cout


def test_cout(capsys):
    # with capsys.disabled():
    cout << "Hello World!"

    # cout.stream.flush()
    # print("Hello World!")
    cap = capsys.readouterr()
    assert cap.out == "Hello World!"
