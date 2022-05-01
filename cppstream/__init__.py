__version__ = "0.1.0"

__all__ = ["Stream", "OutStream", "OutFileStream", "cout", "endl"]

from .base import Stream
from .endl import _Endl
from .out import OutFileStream, OutStream, cout

# cout = _Cout()
endl = _Endl()
