iostream
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

    import iostream

    iostream.cout << "Hello, " << "World!" << iostream.endl

    ostrm = iostream.OutFileStream()

    # or using the context manager 
    with iostream.OutFileStream() as ofs:
        ofs.open("test.txt")
        ofs << "beans" << iostream.endl

See the inheritance diagram:

.. include:: streams.mmd mermaid
