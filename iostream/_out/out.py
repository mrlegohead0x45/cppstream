from __future__ import annotations

from typing import Any

from ..base import Stream


class OutStream(Stream):
    """Class that all out streams inherit from.
    Inherits from Stream"""

    def _write(self, text: str) -> None:
        self.stream.write(text)

    def __lshift__(self, other: Any) -> OutStream:
        if getattr(other, "_iostream_streamable_from", False):
            # tried this but it was infinitely recursive
            # self << other

            other._iostream_stream_from(self)
            val = ""

        else:
            val = str(other)

        self._write(val)
        return self  # so we can chain it e.g cout << 'hello' << ' ' << 'world' << endl
