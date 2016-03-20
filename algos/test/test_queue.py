import unittest
from algos.queue import Queue


class TestQueue(unittest.TestCase):
    def test_push(self):
        q = Queue(1, 2, 3, 4)
        q.push(5)
        self.assertEqual(q, [1, 2, 3, 4, 5])

    def test_pop(self):
        q = Queue(1, 2, 3, 4)
        self.assertEquals(q.pop(), 1)
        self.assertEqual(q, [2, 3, 4])

    def test_empty(self):
        self.assertTrue(Queue().empty())
        self.assertFalse(Queue(1).empty())
