# longest increasing subsequence

def lis(l):
    # step 1: dynamic programming, O(n^2)
    dp = [(0, None)] * len(l)  # list of tuples (size of lis, parent pointer)
    for i in reversed(range(len(l))):
        dp[i] = (1, None)
        for j in range(i+1, len(l)):
            if l[i] <= l[j] and dp[i] <= dp[j]:
                dp[i] = (1+dp[j][0], j)
    # step 2: find beginning of subsequence, O(n)
    print "lis:",
    idx, max = 0, 0
    for i,v in enumerate(dp):
        if max < v[0]:
            idx, max = i, v[0]
    # step 3: print subsequence, O(n)
    while idx is not None:
        print str(l[idx]),
        idx = dp[idx][1]
    print ""

def test():
    l = [
        [7,1,3,5,4,8,1,9,2],
        [1,1,1,1,1,1,1,1,1],
        [9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9],
        [123, 7, 42, 24, 132, 133, 558, 999],
    ]
    for ll in l:
        print ll,
        lis(ll)