# balanced Splay tree
# for reuse of left & right rotates, inherit from AVL trees
from avl import *

class SplayTree(AVLTree):
    """
      Splay trees have the following features:
        1. _No_ metadata needed (compare to colors in RB and heights in AVL)
        2. Each operation, even find, moves (splays) node up to the root
            - benefit: perfect for non-random workloads
        3. Amortized O(lg n) performance, but O(n) worst-case

      Note that insert() and deletenode() are inherted from AVLTree and call rebalance()
    """

    def rebalance(self, node):
        """starting from node, splay node and move upwards; O(lg n)"""
        if node == None:
            return
        parent  = node.parent
        if parent == None:
            # I am root
            self.root = node
            return

        grandpa = parent.parent
        if grandpa == None:
            # zig case: I am child of root
            if parent.left == node:  self.rightrotate(parent)
            else:                    self.leftrotate(parent)
        elif parent.left == node and grandpa.right == parent:
            # zig-zag case: I am left child of right child
            self.rightrotate(parent)
            self.leftrotate(grandpa)
        elif parent.right == node and grandpa.left == parent:
            # zig-zag case (mirrored): I am right child of left child
            self.leftrotate(parent)
            self.rightrotate(grandpa)
        elif parent.left == node and grandpa.left == parent:
            # zig-zig case: I am left child of left child
            self.rightrotate(grandpa)
            self.rightrotate(parent)
        else:
            # zig-zig case (mirrored): I am right child of right child
            self.leftrotate(grandpa)
            self.leftrotate(parent)

        self.rebalance(node)

    def find(self, key):
        "the difference from vanilla BST is the need to rebalance, even if nothing was found"
        if self.root == None:
            return None
        node, parent = self.findpair(key, self.root, None)
        if node == None:  self.rebalance(parent)
        else:             self.rebalance(node)
        return node

    def findmin(self):
        node = BinarySearchTree.findmin(self)
        self.rebalance(node)
        return node

    def findmax(self):
        node = BinarySearchTree.findmax(self)
        self.rebalance(node)
        return node

    def next(self, node):
        node = BinarySearchTree.next(self, node)
        self.rebalance(node)
        return node

    def prev(self, node):
        node = BinarySearchTree.prev(self, node)
        self.rebalance(node)
        return node

    def insertnode(self, node):
        if BinarySearchTree.insertnode(self, node):
            self.rebalance(node)

    def insert(self, key):
        node = Node(key)
        self.insertnode(node)

    def delete(self, key):
        if self.root == None:
            return
        node, parent = self.findpair(key, self.root, None)
        if node == None:  self.rebalance(parent)
        else:             self.deletenode(node)


def sort(a):
    sp = SplayTree()

    for key in a:
        sp.insert(key)

    node = sp.findmin()
    res  = []
    while node:
        res.append(node.key)
        node = sp.next(node)

    # not in-place
    return res