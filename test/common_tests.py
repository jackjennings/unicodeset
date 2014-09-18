class CommonTests(object):

    def test_init_converts_chr_to_unicode(self):
        s = self.klass(['a'])
        assert list(s) == [u"a"]

    def test_init_converts_integer_to_unicode(self):
        s = self.klass([97])
        assert list(s) == [u"a"]

    def test_init_converts_unicode_to_unicode(self):
        s = self.klass([u"\xf9"])
        assert list(s) == [u"\xf9"]

    def test_contains_integer_representation(self):
        s = self.klass(['a'])
        assert 97 in s

    def test_contains_chr_representation(self):
        s = self.klass([u'a'])
        assert 'a' in s

    def test_iterable_order(self):
        s = self.klass(['b', 'c', 'a'])
        assert [u"a", u"b", u"c"] == [c for c in s]

    def test_init_empty_set(self):
        s = self.klass()
        assert [] == list(s)
