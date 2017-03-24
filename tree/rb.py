# balanced Red-Black (RB) tree
# NOTE: RB trees are surprisingly hard to wrap your head around, and I personally
#       dislike them, thus no attempts to make the following code look nice

# for reuse of left & right rotates, inherit RB from AVL trees
from avl import *

class Color:
    Black = 0
    Red = 1

class RBNode(Node):
    def __init__(self, key):
        Node.__init__(self, key)
        self.color = Color.Red  # by agreement, all new nodes are Red

    def __str__(self):
        s = ""
        s += str(self.key) + ":" + str(self.color)
        s += " -> ( "
        s += str(self.left) if self.left  else "--"
        s += " , "
        s += str(self.right) if self.right else "--"
        s += " ) "
        return s


def getcolor(node):
    return node.color if (node and isinstance(node, RBNode)) else Color.Black


class RBTree(AVLTree):
    """
      Red-Black trees have the following four invariants:
       1. Every RBNode has either Black or Red color
       2. Root is always Black; None nodes are always Black
       3. There can be no two adjacent Red nodes (i.e., no parent-child can be both Red)
       4. Each path from any node to leaf has same number of Black nodes
    """

    def rebalanceinsert(self, node):
        """based on RB-Insert-Fixup() from Introduction to Algorithms book"""
        if node == None:
            return

        while getcolor(node.parent) == Color.Red:
            # at this point, node's parent is Red, node's grandpa exists and is Black
            parent  = node.parent
            grandpa = parent.parent
            uncle   = grandpa.left if grandpa.right == parent else grandpa.right

            if getcolor(uncle) == Color.Red:
                # case 1: me, my parent, and my uncle are Red, grandpa is Black
                #         --> enough to recolor and move upwards to check grandpa
                parent.color  = Color.Black
                uncle.color   = Color.Black
                grandpa.color = Color.Red
                node = grandpa
            else:
                # cases 2 & 3: parent is Red, grandpa is Black, and uncle is Black
                #              --> rebalance & recolor them
                if grandpa.left == parent:
                    if parent.right == node:
                        # case 2: left rotate first
                        node = parent
                        self.leftrotate(node)
                    # fall-through to case 3: right rotate and done
                    node.parent.color  = Color.Black
                    node.parent.parent.color = Color.Red
                    self.rightrotate(node.parent.parent)
                else:
                    if parent.left == node:
                        node = parent
                        self.rightrotate(node)
                    node.parent.color  = Color.Black
                    node.parent.parent.color = Color.Red
                    self.leftrotate(node.parent.parent)

        self.root.color = Color.Black

    def insertnode(self, node):
        BinarySearchTree.insertnode(self, node)
        self.rebalanceinsert(node)

    def insert(self, key):
        node = RBNode(key)
        self.insertnode(node)

    def rebalancedelete(self, node, parent):
        """
          based on RB-Delete-Fixup() from Introduction to Algorithms book
          NOTE: we don't use special Nil node, so we add `parent` argument
        """
        if node == None or parent == None:
            return

        while node != self.root and getcolor(node) == Color.Black:
            if node == parent.left:
                sibling = parent.right
                if getcolor(sibling) == Color.Red:
                    # case 1: me and my parent are Black, sibling is Red
                    #         --> recolor & left rotate to make sibling Black and
                    #             fall-through to cases 2-4
                    sibling.color = Color.Black
                    parent.color  = Color.Red
                    self.leftrotate(parent)
                    sibling = parent.right

                if getcolor(sibling.left) == Color.Black and getcolor(sibling.right) == Color.Black:
                    # case 2: me and my sibling are Black, and both his children are Black
                    #         --> recolor sibling to Red, thus removing my double-blackness
                    #             (may lead to two adjacent Reds, so recurse)
                    sibling.color = Color.Red
                    node = parent
                    parent = node.parent
                else:
                    if getcolor(sibling.right) == Color.Black:
                        # case 3: me and my sibling are Black, but his left child is Red
                        #         --> recolor and rotate to make his right child Red and
                        #             fall-through to case 4
                        sibling.left.color = Color.Black
                        sibling.color = Color.Red
                        self.rightrotate(sibling)
                        sibling = parent.right
                    # case 4: me and my sibling are Black, his right child is Red
                    #         --> remove my double-blackness by recoloring & rotation
                    sibling.color       = parent.color
                    parent.color        = Color.Black
                    sibling.right.color = Color.Black
                    self.leftrotate(parent)
                    node = self.root  # for loop-exit condition

            else:
                sibling = parent.left
                if getcolor(sibling) == Color.Red:
                    # case 1: me and my parent are Black, sibling is Red
                    #         --> recolor & right rotate to make sibling Black and
                    #             fall-through to cases 2-4
                    sibling.color = Color.Black
                    parent.color  = Color.Red
                    self.rightrotate(parent)
                    sibling = parent.left

                if getcolor(sibling.left) == Color.Black and getcolor(sibling.right) == Color.Black:
                    # case 2: me and my sibling are Black, and both his children are Black
                    #         --> recolor sibling to Red, thus removing my double-blackness
                    #             (may lead to two adjacent Reds, so recurse)
                    sibling.color = Color.Red
                    node = parent
                    parent = node.parent
                else:
                    if getcolor(sibling.left) == Color.Black:
                        # case 3: me and my sibling are Black, but his right child is Red
                        #         --> recolor and rotate to make his left child Red and
                        #             fall-through to case 4
                        sibling.right.color = Color.Black
                        sibling.color = Color.Red
                        self.leftrotate(sibling)
                        sibling = parent.left
                    # case 4: me and my sibling are Black, his left child is Red
                    #         --> remove my double-blackness by recoloring & rotation
                    sibling.color      = parent.color
                    parent.color       = Color.Black
                    sibling.left.color = Color.Black
                    self.rightrotate(parent)
                    node = self.root  # for loop-exit condition

        node.color = Color.Black

    def deletenode(self, node):
        if node == None:
            return

        removed = node
        removedcolor = getcolor(removed)

        if node.left == None:
            replace = node.right
            replaceparent = node
            self.rewireparent(node, node.right)
        elif node.right == None:
            replace = node.left
            replaceparent = node
            self.rewireparent(node, node.left)
        else:
            removed = self.next(node)
            removedcolor = getcolor(removed)

            replace = removed.right
            replaceparent = removed

            if removed.parent != node:
                self.rewireparent(removed, removed.right)
                removed.right = node.right
                node.right.parent = removed

            self.rewireparent(node, removed)
            removed.left = node.left
            removed.left.parent = removed
            removed.color = node.color

        self.updatesizes(node)

        if removedcolor == Color.Black:
            self.rebalancedelete(replace, replaceparent)

def sort(a):
    rb = RBTree()

    for key in a:
        rb.insert(key)

    node = rb.findmin()
    res  = []
    while node:
        res.append(node.key)
        node = rb.next(node)

    # not in-place
    return res