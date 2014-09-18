unicodeset
==========

unicodeset is a small module for managing sets of unique unicode code points.

The classes ``UnicodeSet`` and ``FrozenUnicodeSet`` as superclasses of the respective Python builtins.

.. code-block:: python

    from unicodeset import UnicodeSet, FrozenUnicodeSet

Values can be passed in as either integers or strings (or unicode strings in Python 2.7).

.. code-block:: python

    >>> s = UnicodeSet(['a', 98, u'c'])
    UnicodeSet([u'a', u'b', u'c'])

Inclusion can be checked using either an integer or string representations.

.. code-block:: python

    >>> s = UnicodeSet([u'a', u'b', u'c'])
    >>> 98 in s
    True
    >>> 'b' in s
    True

Iterating over UnicodeSet returns values sorted by code point.

.. code-block:: python

    >>> [c for c in UnicodeSet(['z', 'n', '$', 'a'])]
    [u'$', u'a', u'n', u'z']

Supports Python 2.6 – 3.x