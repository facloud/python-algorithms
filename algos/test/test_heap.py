import unittest

from hypothesis import given
from hypothesis.strategies import integers

from algos.heap import HeapTree, HeapList
from algos.perf.rnd_data_gen import RandomDatasetGenerator
from algos.tree import Node


class TestHeapTree(unittest.TestCase):
    def setUp(self):
        self.gen = RandomDatasetGenerator()

    def assertMinHeap(self, node):
        if len(node.children) > 0 and node.children[0] < node.value:
            raise self.failureException(
                'left child ({}) is smaller than parent'.format(
                    node.children[0].value
                )
            )

        if len(node.children) > 1 and node.children[1] < node.value:
            raise self.failureException(
                'right child ({}) is smaller than parent'.format(
                    node.children[1].value
                )
            )

    @given(integers(min_value=10, max_value=100))
    def test_insert_node(self, size):
        data = self.gen.get_unsorted_list(size)

        tree = HeapTree(data[0])
        for i in range(1, size):
            tree.insert_node(Node(data[i]))
        from algos.tree_visualization import draw_tree

        self.assertMinHeap(tree)

class TestHeapList(unittest.TestCase):
    def setUp(self):
        self.gen = RandomDatasetGenerator()

    def assertMinHeap(self, collection):
        for i in range(0, len(collection)/2):
            if 2*i < len(collection) and collection[i] > collection[2*i]:
                raise self.failureException(
                    'left child ({}) is smaller than parent'.format(
                        collection[2*i]
                    )
                )

            if 2*i+1 < len(collection) and collection[i] > collection[2*i+1]:
                raise self.failureException(
                    'left child ({}) is smaller than parent'.format(
                        collection[2*i+1]
                    )
                )

    @given(integers(min_value=10, max_value=100))
    def test_append(self, size):
        data = self.gen.get_unsorted_list(size)

        l = HeapList()
        for i in range(0, size):
            l.append(data[i])

        self.assertMinHeap(l)
