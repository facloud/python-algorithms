import unittest

from hypothesis import given
from hypothesis.strategies import integers

from algos import math


class TestMath(unittest.TestCase):
    @given(
        integers(min_value=1, max_value=100),
        integers(min_value=1, max_value=10)
    )
    def test_pow(self, x, y):
        self.assertEquals(math.pow(x, y), pow(x, y))
