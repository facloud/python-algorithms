from algos.queue import Queue


class Node(object):
    def __init__(self, value, parent=None, children=[]):
        self.value = value
        self.parent = parent
        self.children = children[:]

    def set_parent(self, parent):
        self.parent = parent

    def register_child(self, child):
        self.children.append(child)
        child.set_parent(self)

    def __eq__(self, other):
        return self.value == other.value


class Tree(Node):
    @classmethod
    def from_node(klass, node):
        return klass(node.value, node.children[:])

    def __init__(self, value, children=[]):
        Node.__init__(self, value, None, children[:])

    def run_breadth_first_traversal(self, cb):
        """Run a Depth first traversal and call the callback for every node.

        The callback can return anything but None. When the callback returns
        None, the traversal continues to deeper levels of the tree.
        """
        q = Queue(self)
        while not q.empty():
            node = q.pop()

            ret_val = cb(node)
            if ret_val is not None:
                return ret_val

            for child in node.children:
                q.push(child)

        return None

    def run_depth_first_traversal(self, cb):
        """Run a Depth first traversal and call the callback for every node.

        The callback can return anything but None. When the callback returns
        None, the traversal continues to deeper levels of the tree.
        """
        ret_val = cb(self)
        if ret_val is not None:
            return ret_val

        for child in self.children:
            child_tree = Tree.from_node(child)

            ret_val = child_tree.run_depth_first_traversal(cb)
            if ret_val is not None:
                return ret_val

        return None


class BinaryTree(Tree):
    def insert_node(self, node):
        q = Queue(self)
        while not q.empty():
            parent_node = q.pop()
            if len(parent_node.children) < 2:
                parent_node.register_child(node)
                break
            for child in parent_node.children:
                q.push(child)
