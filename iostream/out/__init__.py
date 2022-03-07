__all__ = ["OutStream", "OutFileStream", "cout"]

from .._out.cout import _Cout
from .._out.fout import OutFileStream
from .._out.out import OutStream

cout = _Cout()
