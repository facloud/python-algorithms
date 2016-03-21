import unittest
from hypothesis import given
from hypothesis.strategies import integers, random_module
from algos.perf.rnd_data_gen import RandomDatasetGenerator


class TestRandomDatasetGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = RandomDatasetGenerator()

    def assertSorted(self, collection):
        for i in range(1, len(collection)):
            if collection[i] < collection[i-1]:
                msg = "element '{}' of index {} is bigger".format(
                    collection[i-1], i-1
                ) \
                    + " than element '{}' of index {}".format(collection[i], i)
                raise self.failureException(msg)

    def assertNotSorted(self, collection):
        for i in range(1, len(collection)):
            if collection[i] < collection[i-1]:
                return
        raise self.failureException('collection is sorted')

    @given(integers(min_value=10, max_value=100))
    def test_get_sorted_list(self, size):
        l = self.gen.get_sorted_list(size)
        self.assertSorted(l)

    @given(integers(min_value=10, max_value=100))
    def test_get_unsorted_list(self, size):
        l = self.gen.get_unsorted_list(size)
        self.assertNotSorted(l)

    @given(integers(min_value=10, max_value=100))
    def test_get_existant_el(self, size):
        l = self.gen.get_sorted_list(size)
        el = self.gen.get_existant_el(l)
        self.assertIn(el, l)

        l = self.gen.get_unsorted_list(size)
        el = self.gen.get_existant_el(l)
        self.assertIn(el, l)

    @given(integers(min_value=10, max_value=100))
    def test_get_non_existant_el_sorted(self, size):
        l = self.gen.get_sorted_list(size)
        el = self.gen.get_non_existant_el_sorted(l)
        self.assertNotIn(el, l)

    @given(integers(min_value=10, max_value=100))
    def test_get_non_existant_el_unsorted(self, size):
        l = self.gen.get_unsorted_list(size)
        el = self.gen.get_non_existant_el_unsorted(l)
        self.assertNotIn(el, l)
