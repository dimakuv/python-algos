# merge sort

def sort(a):
	if len(a) == 1:
		return a

	# step 1: sort left and right recursively
	l, r = sort(a[:len(a)/2]), sort(a[len(a)/2:])

	# step 2: use two-finger traversal to combine l and r
	res = []
	li, ri = 0, 0
	while li < len(l) and ri < len(r):
		if l[li] <= r[ri]:
			res.append(l[li])
			li += 1
		else:
			res.append(r[ri])
			ri += 1

	# step 3: add the rest from l or r
	if li < len(l):
		res.extend(l[li:])
	if ri < len(r):
		res.extend(r[ri:])

	# it was clearly not in-place
	return res