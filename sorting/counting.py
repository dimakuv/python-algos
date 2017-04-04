# counting sort (simple one-digit int)

DIGITS = 10

def sort(a, digit = 0):
    freq = []
    for k in range(DIGITS):
        freq.append(0)

    # frequency of each digit in a + init res
    res = []
    for i in range(len(a)):
        d = (a[i]/10**digit) % DIGITS
        freq[d] += 1
        res.append(0)

    # cummulative frequency of each digit
    for k in range(1, len(freq)):
        freq[k] += freq[k-1]

    # reverse-populate res array based on cummulated frequencies
    #   (reverse to preserve stability)
    for i in reversed(xrange(len(a))):
        d = (a[i]/10**digit) % DIGITS
        freq[d] -= 1
        idx = freq[d]
        res[idx] = a[i]

    # it was clearly not in-place
    return res