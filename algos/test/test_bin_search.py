import unittest

from hypothesis import given
from hypothesis.strategies import integers

from algos import bin_search


ARRAY_LENGTH = 100000


class TestBinarySearch(unittest.TestCase):
    @given(integers(min_value=0, max_value=ARRAY_LENGTH-1))
    def test_bs_contains(self, x):
        self.assertTrue(bin_search.bs_contains(range(ARRAY_LENGTH), x))

    @given(integers(min_value=ARRAY_LENGTH))
    def test_bs_doesnt_contain(self, x):
        self.assertFalse(bin_search.bs_contains(range(ARRAY_LENGTH), x))

    @given(integers(min_value=0, max_value=ARRAY_LENGTH-1))
    def test_bs_insert_existing(self, x):
        l = range(ARRAY_LENGTH)
        l = bin_search.bs_insert(l, x)
        self.assertEqual(l[x], x)

    @given(integers(min_value=0, max_value=ARRAY_LENGTH-1))
    def test_bs_insert_not_existing(self, x):
        l = range(ARRAY_LENGTH)
        del l[x]
        l = bin_search.bs_insert(l, x)
        self.assertEqual(l[x], x)

    @given(integers(min_value=ARRAY_LENGTH))
    def test_bs_insert_in_end(self, x):
        l = range(ARRAY_LENGTH)
        l = bin_search.bs_insert(l, x)
        self.assertEqual(l[ARRAY_LENGTH], x)

if __name__ == '__main__':
    unittest.main()
