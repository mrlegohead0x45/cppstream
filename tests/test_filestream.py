from tempfile import NamedTemporaryFile

from cppstream import FileStream


def test_filestream_linesep():
    stream = FileStream()
    assert stream.linesep == "\n"


def test_filestream_closed_by_default():
    stream = FileStream()
    assert not stream.is_open


def test_filestream_default_mode():
    stream = FileStream()
    assert stream.default_mode == "r"


def test_filestream_is_open_when_opened():
    stream = FileStream()
    with NamedTemporaryFile(delete=False) as f:
        stream.open(f.name)

        assert stream.is_open
        stream.close()


def test_filestream_is_closed_when_closed():
    stream = FileStream()
    with NamedTemporaryFile(delete=False) as f:
        stream.open(f.name)
        stream.close()

        assert not stream.is_open


def test_filestream_constructor_opens():
    with NamedTemporaryFile(delete=False) as f:
        stream = FileStream(f.name)
        assert stream.is_open
        stream.close()


def test_filestream_context_manager_opens():
    with NamedTemporaryFile(delete=False) as f:
        with FileStream(f.name) as stream:
            assert stream.is_open
