# quicksort

def quicksort(a, lo, hi):
	"""actual recursive quicksort implementation (Lomuto scheme)"""
	if hi - lo <= 0:
		return

	# step 1: find pivot, move smaller items to left, bigger -- to right of pivot
	pivot = a[hi]  # last item initially

	li, ri = lo, hi-1
	while True:
		while a[li] <= pivot and li < hi:  li += 1
		while a[ri] >= pivot and ri > lo:  ri -= 1

		if li >= ri:  break

		a[li], a[ri] = a[ri], a[li]

	a[hi], a[li] = a[li], a[hi]  # finally move pivot

	# step 2: recursively quicksort left and right (w/o pivot point)
	quicksort(a, lo, li-1)
	quicksort(a, li+1, hi)


def sort(a):
	quicksort(a, 0, len(a)-1)
	# it was in-place
	return a