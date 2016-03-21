import unittest
from algos.tree import Tree, Node, BinaryTree, Heap
from algos.tree_visualization import draw_tree
from algos.queue import Queue
from algos.perf.rnd_data_gen import RandomDatasetGenerator


class TestNode(unittest.TestCase):
    def test_set_parent(self):
        p = Node(1)
        n = Node(12)
        self.assertIsNone(n.parent)

        n.set_parent(p)
        self.assertEquals(n.parent, p)

    def test_equality(self):
        self.assertTrue(Node(12) == Node(12))
        self.assertFalse(Node(12) == Node(13))

    def test_register_child(self):
        p = Node(1)
        self.assertListEqual(p.children, [])

        n = Node(12)
        self.assertIsNone(n.parent)

        p.register_child(n)
        self.assertListEqual(p.children, [n])
        self.assertEqual(n.parent, p)


class TestTree(unittest.TestCase):
    def make_tree(self, collection):
        if len(collection) == 0:
            return None

        q = Queue()
        root_node = Tree(collection[0])
        tree = root_node
        for c in collection[1:]:
            if len(root_node.children) == 2:
                root_node = q.pop()
            n = Node(c)
            root_node.register_child(n)
            q.push(n)

        return tree

    def test_init(self):
        self.assertIsNone(Tree(12).parent)

        p = Node(1)
        n = Node(12)
        p.register_child(n)
        self.assertIsNone(Tree.from_node(n).parent)

    def test_breadth_first_traversal(self):
        tree = self.make_tree(range(0, 7))

        l = []

        def cb(node):
            l.append(node.value)

        tree.run_breadth_first_traversal(cb)
        self.assertListEqual(l, [0, 1, 2, 3, 4, 5, 6])

    def test_depth_first_traversal(self):
        tree = self.make_tree(range(0, 7))

        l = []

        def cb(node):
            l.append(node.value)

        tree.run_depth_first_traversal(cb)
        self.assertListEqual(l, [0, 1, 3, 4, 2, 5, 6])


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.gen = RandomDatasetGenerator()

    def test(self):
        ARRAY_LENGTH = 100
        data = self.gen.get_unsorted_list(ARRAY_LENGTH)

        tree = BinaryTree(data[0])
        for i in range(1, ARRAY_LENGTH):
            tree.insert_node(Node(data[i]))

        l = []

        def cb(node):
            l.append(node.value)

        tree.run_breadth_first_traversal(cb)
        self.assertListEqual(l, data)
