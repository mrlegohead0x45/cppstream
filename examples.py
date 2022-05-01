import cppstream

# basic examples
cppstream.cout << "hello world" << cppstream.endl
cppstream.cout << 5 << "\n"
s = "hello world\n"
cppstream.cout << s


# example of a streamable type
class ExampleStreamableType:
    _iostream_streamable_from = True
    value = 8

    def _iostream_stream_from(self, ostream: cppstream.OutStream):
        ostream << "hello from ExampleStreamableType" << cppstream.endl
        ostream << "value is " << self.value

    # binary left shift still usable
    def __lshift__(self, other: int):
        return self.value << other


var = ExampleStreamableType()
cppstream.cout << var << cppstream.endl


# files
ofs = cppstream.OutFileStream()
ofs.open("test.txt")
ofs << "hello world\n"
ofs.close()

# it has a context manager too
with cppstream.OutFileStream() as ofs:
    ofs.open("test.txt", "a")
    ofs << "hello from the outfilestream context manager" << cppstream.endl
