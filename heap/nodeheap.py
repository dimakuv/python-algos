# abstract heap, minheap, and maxheap -- implementations using Node objects
#   NOTE: with Node objects, can support delete() operation with O(lg n)

class Node(object):
    __slots__ = ['value', 'heap', 'idx']
    def __init__(self, value):
        self.value = value

def parent(i):
    return (i-1)//2

def left(i):
    return i*2+1

def right(i):
    return i*2+2

class AbstractHeap(object):
    def __init__(self):
        self.a = []

    def compare(self, l, r):
        raise NotImplementedError("AbstractHeap does not implement comparison!")

    def swap(self, i, j):
        self.a[i].idx = j
        self.a[j].idx = i
        self.a[i], self.a[j] = self.a[j], self.a[i]

    def upheap(self, i):
        if i == 0:  return
        p = parent(i)
        if self.compare(self.a[i], self.a[p]):
            self.swap(i, p)
            self.upheap(p)

    def downheap(self, i):
        l, r = left(i), right(i)
        toswap = i
        if l < len(self.a) and self.compare(self.a[l], self.a[toswap]):
            toswap = l
        if r < len(self.a) and self.compare(self.a[r], self.a[toswap]):
            toswap = r
        if toswap != i:
            self.swap(i, toswap)
            self.downheap(toswap)

    def insert(self, v):
        i = len(self.a)
        v.heap = self
        v.idx  = i
        self.a.append(v)
        self.upheap(i)

    def peek(self):
        return self.a[0].value if len(self.a) > 0 else 1000

    def extract(self):
        if len(self.a) == 1:  return self.a.pop()
        res = self.a[0]
        self.a[0] = self.a.pop()
        self.downheap(0)
        return res

    def delete(self, node):
        idx = node.idx
        if idx == len(self.a)-1:
            self.a.pop()
            return
        self.swap(idx, len(self.a)-1)
        self.a.pop()
        if idx != 0 and self.compare(self.a[idx], self.a[parent(idx)]):
            self.upheap(idx)
        else:
            self.downheap(idx)

class MaxHeap(AbstractHeap):
    def compare(self, l, r):
        return l.value > r.value

class MinHeap(AbstractHeap):
    def compare(self, l, r):
        return l.value < r.value
