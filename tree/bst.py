# simple unbalanced Binary Search Tree (BST)

class Node(object):

    def __init__(self, key):
        self.parent = None
        self.left   = None
        self.right  = None
        self.size   = 1
        self.key    = key

    def __str__(self):
        s = ""
        s += str(self.key)
        s += " -> ( "
        s += str(self.left)  if self.left  else "--"
        s += " , "
        s += str(self.right) if self.right else "--"
        s += " ) "
        return s


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def __find(self, key, node, parent):
        """return a pair <found Node or None, parent>"""
        if node == None:
            return (None, parent)
        if key == node.key:
            return (node, parent)
        elif key < node.key:
            return self.__find(key, node.left, node)
        else:
            return self.__find(key, node.right, node)

    def find(self, key):
        """return found Node or None"""
        if self.root == None:
            return None
        return self.__find(key, self.root, None)[0]

    def __findmin(self, node):
        while node and node.left:
            node = node.left
        return node

    def findmin(self):
        return self.__findmin(self.root)

    def __findmax(self, node):
        while node and node.right:
            node = node.right
        return node

    def findmax(self):
        return self.__findmax(self.root)

    def next(self, node):
        if node == None:
            return None
        if node.right:
            return self.__findmin(node.right)
        while node.parent and node.parent.left != node:
            node = node.parent
        return node.parent

    def prev(self, node):
        if node == None:
            return None
        if node.left:
            return self.__findmax(node.left)
        while node.parent and node.parent.right != node:
            node = node.parent
        return node.parent

    def __updatesizes(self, node):
        while node and node.parent:
            node = node.parent
            node.size = 1
            if node.left:
                node.size += node.left.size
            if node.right:
                node.size += node.right.size

    def insertnode(self, node):
        """insert node in BST if no existing node already"""
        assert node == None or type(node) is Node

        if self.root == None:
            self.root = node

        found, parent = self.__find(node.key, self.root, None)
        if found:
            return

        assert parent != None
        node.parent = parent
        if node.key < parent.key:
            assert parent.left == None
            parent.left = node
        else:
            assert parent.right == None
            parent.right = node

        self.__updatesizes(node)

    def insert(self, key):
        node = Node(key)
        self.insertnode(node)

    def __rewireparent(self, node, newnode):
        """detach node and make a link between node.parent and newnode"""
        if newnode:
            newnode.parent = node.parent
        if node == self.root:
            self.root = newnode
            return
        if node.parent.left == node:
            node.parent.left = newnode
        else:
            node.parent.right = newnode

    def deletenode(self, node):
        if node == None:
            return
        if node.left == None and node.right == None:
            self.__rewireparent(node, None)
        elif node.left and node.right == None:
            self.__rewireparent(node, node.left)
        elif node.left == None and node.right:
            self.__rewireparent(node, node.right)
        else:
            replace = self.next(node)
            self.deletenode(replace)
            self.__rewireparent(node, replace)

            replace.left = node.left
            if node.left:
                node.left.parent = replace
            replace.right = node.right
            if node.right:
                node.right.parent = replace

        self.__updatesizes(node)

    def delete(self, key):
        node = self.find(key)
        self.deletenode(node)

    def size(self):
        """total number of nodes in the tree"""
        if self.root == None:
            return 0
        return self.root.size

    def rank(self, key):
        """return number of nodes less than or equal to key"""
        res = 0

        node = self.root
        while node:
            if key < node.key:
                node = node.left
            else:
                res += 1
                if node.left:
                    res += node.left.size
                if key == node.key:
                    break
                node = node.right

        return res

    def __str__(self):
        return str(self.root) + "."


def sort(a):
    bst = BinarySearchTree()

    for key in a:
        bst.insert(key)

    node = bst.findmin()
    res  = []
    while node:
        res.append(node.key)
        node = bst.next(node)

    # not in-place
    return res