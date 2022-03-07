iostream
--------

This is a library that implements C++-style IO with streams in Python

For example

.. code:: cpp

    #include <iostream>
    // ...
    std::cout << "Hello, " << "World!" << std::endl;

translates to

.. code:: python

    import iostream
    iostream.cout << "Hello, " << "World!" << iostream.endl

See the inheritance diagram:

.. include:: streams.mmd mermaid
