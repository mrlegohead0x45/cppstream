from cppstream import OutFileStream


def test_outfilestream_default_mode():
    stream = OutFileStream()
    assert stream.default_mode == "w"
