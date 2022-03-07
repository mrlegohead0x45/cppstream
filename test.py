import iostream

iostream.cout << "beans" << iostream.endl

# iostream.cout << 5 << "\n"


class Beans:
    _iostream_streamable_from = True

    def _iostream_stream_from(self, ostream: iostream.OutStream):
        ostream << "beans"


# iostream._out.cout._Cout()

iostream.cout << Beans() << iostream.endl

with iostream.OutFileStream() as ofs:
    ofs.open("test.txt")
    ofs << "beans" << iostream.endl
