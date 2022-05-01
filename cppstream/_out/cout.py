from sys import stdout

from .out import OutStream


class _Cout(OutStream):
    """Class that represents std::cout and writes to stdout
    Inherits from Out"""

    _stream = stdout
