# from typing import IO, Optional

from ..base import FileStream
from .out import OutStream


class OutFileStream(FileStream, OutStream):
    _default_mode = "w"
