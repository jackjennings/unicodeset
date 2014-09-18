__version__ = "0.1.0"
__all__ = ["UnicodeSet", "FrozenUnicodeSet"]


def _encode(iterable):
    if iterable is None:
        iterable = []
    return [_encode_char(c) for c in iterable]


def _encode_char(char):
    if isinstance(char, int):
        try:
            return unichr(char)
        except Exception:
            return chr(char)
    else:
        try:
            return unicode(char)
        except Exception:
            return char


class BaseUnicodeSet(object):

    def __init__(self, iterable=None):
        super(BaseUnicodeSet, self).__init__(_encode(iterable))

    def __contains__(self, char):
        return super(BaseUnicodeSet, self).__contains__(_encode_char(char))

    def __iter__(self):
        return iter(sorted(set(self), key=ord))


class UnicodeSet(BaseUnicodeSet, set):
    pass


class FrozenUnicodeSet(BaseUnicodeSet, frozenset):

    def __new__(cls, iterable=None):
        return frozenset.__new__(cls, _encode(iterable))

    def __init__(self, iterable=None):
        pass
