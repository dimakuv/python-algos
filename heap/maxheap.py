# maxheap

from abstractheap import *

class MaxHeap(AbstractHeap):
	"""priority queue using maxheap"""

	def compare(self, l, r):
		return l > r


def sort(a):
	heap = MaxHeap(a)

	for i in reversed(xrange(len(a))):
		heap.buildmaxheap()
		a[i] = heap.extract()

	return a