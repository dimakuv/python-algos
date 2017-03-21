# abstract heap

def parent(i):
	return (i-1)/2

def left(i):
	return i*2+1

def right(i):
	return i*2+2


class AbstractHeap(object):
	"""priority queue using heap (abstract parent class)"""

	def __init__(self, a = None):
		self.a = a[:] if a else []  # copy list if provided

	def compare(self, l, r):
		raise NotImplementedError("AbstractHeap does not implement comparison!")

	def upheap(self, i):
		if i == 0:  return
		p = parent(i)
		if self.compare(self.a[i], self.a[p]):
			self.a[i], self.a[p] = self.a[p], self.a[i]
			self.upheap(p)

	def downheap(self, i):
		# assumption: subtrees at left & right children are maxheaps already
		l, r = left(i), right(i)
		toswap = i
		if l < len(self.a) and self.compare(self.a[l], self.a[toswap]):
			toswap = l
		if r < len(self.a) and self.compare(self.a[r], self.a[toswap]):
			toswap = r

		if toswap != i:
			self.a[i], self.a[toswap] = self.a[toswap], self.a[i]
			self.downheap(toswap)

	def buildmaxheap(self):
		lastparent = parent(len(self.a)-1)
		for i in reversed(xrange(lastparent+1)):
			# traverse from last parent to root to downheap subtrees
			self.downheap(i)

	def insert(self, v):
		i = len(self.a)
		self.a.append(v)
		self.upheap(i)

	def peek(self):
		return self.a[0] if len(self.a) > 0 else None

	def extract(self):
		if len(self.a) == 0:  return None
		if len(self.a) == 1:  return self.a.pop()

		res = self.a[0]
		self.a[0] = self.a.pop()
		self.downheap(0)

		return res

	def empty(self):
		return len(self.a) == 0

	def __str__(self):
		return str(self.a)
