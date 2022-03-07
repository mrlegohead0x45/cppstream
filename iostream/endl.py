from .out import OutStream


class _Endl:
    _iostream_streamable_from = True

    def __init__(self) -> None:
        pass

    def _iostream_stream_from(self, ostream: OutStream) -> None:
        ostream.stream.flush()
        ostream << ostream.linesep
