from BTreeNode import BTreeNode


class BTree:

    def __init__(self, order):
        self.order = order
        self.order -= 1
        self.root = BTreeNode(True)

    def insert(self, key):
        """
            insert key in BTree
        """
        root = self.root

        # if the node was full
        if len(root.keys) == 2 * self.order - 1:
            btn = BTreeNode()
            self.root = btn
            btn.child.insert(0, root)
            self._split_child(btn, 0)
            self._insert_when_is_not_full(btn, key)
        else:
            self._insert_when_is_not_full(root, key)

    def _split_child(self, parent, index):
        """
            splits the child of node at 'parent' from index 'index'
        """
        order = self.order
        y = parent.child[index]
        z = BTreeNode(y.leaf)
        parent.child.insert(index + 1, z)
        parent.keys.insert(index, y.keys[order - 1])
        z.keys = y.keys[order: (2 * order) - 1]
        y.keys = y.keys[0: order - 1]
        if not y.leaf:
            z.child = y.child[order: 2 * order]
            y.child = y.child[0: order - 1]

    def _insert_when_is_not_full(self, index, key):
        """
            insert a key when the node is not full
        """

        i = len(index.keys) - 1
        if index.leaf:
            index.keys.append((None, None))
            while i >= 0 and key < index.keys[i]:
                index.keys[i + 1] = index.keys[i]
                i -= 1
            index.keys[i + 1] = key
        else:
            while i >= 0 and key < index.keys[i]:
                i -= 1
            i += 1
            if len(index.child[i].keys) == (2 * self.order) - 1:
                self._split_child(index, i)
                if key > index.keys[i]:
                    i += 1
            self._insert_when_is_not_full(index.child[i], key)

    def traverse(self, node):
        print('(', end=' ')
        for key in node.keys:
            print(key, end=' ')
        print(')', end=' ')
        for ch in node.child:
            self.traverse(ch)

    def delete(self, key):
        pass
