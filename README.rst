cppstream
--------

This is a library that implements C++-style IO with streams in Python

For example

.. code:: cpp

    #include <iostream>
    #include <fstream>
    std::cout << "Hello, " << "World!" << std::endl;

    std::ofstream ostrm("test.txt");
    ostrm << "Hello, World!" << std::endl;

translates to

.. code:: python

    import cppstream

    cppstream.cout << "Hello, " << "World!" << cppstream.endl

    ostrm = cppstream.OutFileStream()

    # or using the context manager 
    with cppstream.OutFileStream() as ofs:
        ofs.open("test.txt")
        ofs << "beans" << cppstream.endl

See the inheritance diagram:

.. image:: streams.png
