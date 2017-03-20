# insertion sort

def sort(a):
	for i in xrange(len(a)):
		curr = a[i]
		for j in reversed(xrange(i)):
			if a[j] < curr:
				# found the biggest item from right in sorted part
				a[j+1] = curr
				break
			a[j+1] = a[j]
		else:
			# traversed the whole sorted part -> curr is smallest
			a[0] = curr

	# it was in-place sort
	return a