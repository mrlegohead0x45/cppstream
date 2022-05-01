from __future__ import annotations

from os import linesep
from typing import IO, AnyStr, Optional


class Stream:
    """Class that all stream objects inherit from"""

    _linesep: AnyStr = linesep
    _stream: IO

    def __init__(self) -> None:
        pass

    @property
    def linesep(self) -> str:
        return self._linesep

    @property
    def stream(self) -> IO:
        return self._stream


class FileStream(Stream):
    _linesep = "\n"
    _is_open: bool = False
    _default_mode = "r"

    def __init__(self, fileobj: Optional[IO] = None) -> None:
        if fileobj is not None:
            self._stream = fileobj

    def __enter__(self) -> FileStream:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()

    def open(self, path: str, mode: Optional[str] = None) -> None:
        self._stream = open(path, mode=mode or self.default_mode)
        self._is_open = True

    def close(self) -> None:
        self._is_open = False
        self.stream.flush()
        self.stream.close()

    @property
    def is_open(self) -> bool:
        return self._is_open

    @property
    def default_mode(self) -> str:
        return self._default_mode
