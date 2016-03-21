from algos.tree import Node, BinaryTree


def exchange_nodes(a, b):
    temp_val = a.value
    a.value = b.value
    b.value = temp_val


class HeapTree(BinaryTree):
    def min_heapify(self, node):
        """The heap property is that parent.value <= left.value
        and parent.value <= right.value.
        """
        left = node.children[0] if len(node.children) > 0 else None
        right = node.children[1] if len(node.children) > 1 else None

        smallest = node
        if left is not None and left.value < smallest.value:
            smallest = left
        if right is not None and right.value < smallest.value:
            smallest = right

        if smallest is not node:
            exchange_nodes(smallest, node)
            self.min_heapify(node)

    def insert_node(self, node):
        BinaryTree.insert_node(self, node)
        while node is not None:
            self.min_heapify(node)
            node = node.parent


class HeapList(list):
    def exchange_elements(self, a, b):
        temp = self[a]
        self[a] = self[b]
        self[b] = temp

    def min_heapify(self, idx):
        left = self[2*idx] if len(self) > 2*idx else None
        right = self[2*idx+1] if len(self) > 2*idx+1 else None

        smallest = idx
        if left is not None and left < self[smallest]:
            smallest = 2*idx
        if right is not None and right < self[smallest]:
            smallest = 2*idx + 1

        if smallest is not idx:
            self.exchange_elements(smallest, idx)
            self.min_heapify(idx)

    def append(self, el):
        list.append(self, el)
        for i in range(len(self)/2, -1, -1):
            self.min_heapify(i)
