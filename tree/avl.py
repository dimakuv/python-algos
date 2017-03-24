# balanced AVL tree

from bst import *

class AVLNode(Node):
    def __init__(self, key):
        Node.__init__(self, key)
        self.height = 0


def getheight(node):
    return node.height if (node and isinstance(node, AVLNode)) else -1


class AVLTree(BinarySearchTree):

    def leftrotate(self, x):
        """change subtree of form x->(A, y->(B,C)) to y->(x->(A,B), C);  O(1)"""
        if x == None or x.right == None:
            return
        y = x.right
        self.rewireparent(x, y)
        x.parent = y
        x.right  = y.left
        y.left   = x
        if x.right:
            x.right.parent = x

    def rightrotate(self, y):
        """change subtree of form y->(x->(A,B), C) to x->(A, y->(B,C));  O(1)"""
        if y == None or y.left == None:
            return
        x = y.left
        self.rewireparent(y, x)
        y.parent = x
        y.left   = x.right
        x.right  = y
        if y.left:
            y.left.parent = y

    def rebalance(self, node):
        """starting from node, fix AVL property if violated and move upwards; O(lg n)"""
        if node == None:
            return

        if abs(getheight(node.left) - getheight(node.right)) > 1:
            # violated property of "height of one child at most one greater than of another"
            if getheight(node.right) > getheight(node.left):
                if getheight(node.right.right) >= getheight(node.right.left):
                    # node.right is right-heavy (or balanced): straight-line simple case
                    self.leftrotate(node)
                else:
                    # node.right is left-heavy: zigzag complex case
                    self.rightrotate(node.right)
                    self.leftrotate(node)
            else:
                if getheight(node.left.left) >= getheight(node.left.right):
                    # node.left is left-heavy (or balanced): straight-line simple case
                    self.rightrotate(node)
                else:
                    # node.left is right-heavy: zigzag complex case
                    self.leftrotate(node.left)
                    self.rightrotate(node)

        node.height = max(getheight(node.left), getheight(node.right)) + 1
        self.rebalance(node.parent)

    def insertnode(self, node):
        BinarySearchTree.insertnode(self, node)
        self.rebalance(node)

    def insert(self, key):
        node = AVLNode(key)
        self.insertnode(node)

    def deletenode(self, node):
        if node == None:
            return

        rebalancenode = None
        if node.left == None or node.right == None:
            # simple cases of node del: rebalance starting from node's parent
            rebalancenode = node.parent
        else:
            # complex case with two children: rebalance starting from next()'s parent
            rebalancenode = self.next(node)
            if rebalancenode:
                rebalancenode = rebalancenode.parent

        BinarySearchTree.deletenode(self, node)
        self.rebalance(rebalancenode)


def sort(a):
    avl = AVLTree()

    for key in a:
        avl.insert(key)

    node = avl.findmin()
    res  = []
    while node:
        res.append(node.key)
        node = avl.next(node)

    # not in-place
    return res