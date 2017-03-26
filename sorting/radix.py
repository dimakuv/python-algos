# radix sort (simple, up to 1,000)

# radix relies on counting for one-digit sort
import counting

DIGITS = 3

def sort(a):
	for i in range(DIGITS):
		a = counting.sort(a, i)

	return a


testlist = [123, 321, 58, 255, 1, 0, 132, 59, 254]