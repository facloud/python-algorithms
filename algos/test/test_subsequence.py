import random
import unittest

from hypothesis import given
from hypothesis.strategies import integers, random_module

from algos.perf.rnd_data_gen import RandomDatasetGenerator
from algos.subsequence import is_subsequence


ARRAY_LENGTH = 100


class TestIsSubsequence(unittest.TestCase):
    def test_simple_input(self):
        self.assertTrue(is_subsequence([], []))
        self.assertFalse(is_subsequence([1, 2], [1, 2, 3]))
        self.assertFalse(is_subsequence([1, 2, 3], [1, 3]))
        self.assertTrue(is_subsequence([1, 2, 3], [1, 2]))
        self.assertTrue(is_subsequence([1, 2, 3], [2, 3]))

    @given(
        integers(min_value=20, max_value=ARRAY_LENGTH-1),
        random_module()
    )
    def test_complex_input_true(self, size, rnd):
        gen = RandomDatasetGenerator(rnd.seed)
        l = gen.get_unsorted_list(size)

        start_idx = random.randint(0, size-10)
        end_idx = random.randint(start_idx+1, size)

        self.assertTrue(is_subsequence(l, l[start_idx:end_idx]))

    @given(
        integers(min_value=50, max_value=ARRAY_LENGTH-1),
        random_module()
    )
    def test_complex_input_false(self, size, rnd):
        gen = RandomDatasetGenerator(rnd.seed)
        l = gen.get_unsorted_list(size)

        start_idx = random.randint(0, size-20)
        end_idx = random.randint(start_idx+10, size-1)
        subseq = l[start_idx:end_idx]
        subseq[end_idx-start_idx-1] += 12

        self.assertFalse(is_subsequence(l, subseq))
