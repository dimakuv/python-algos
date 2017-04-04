# maxheap

from abstractheap import *

class MinHeap(AbstractHeap):
    """priority queue using minheap"""

    def compare(self, l, r):
        return l < r


def sort(a):
    heap = MinHeap(a)

    for i in range(len(a)):
        heap.buildmaxheap()
        a[i] = heap.extract()

    return a