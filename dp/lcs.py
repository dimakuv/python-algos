# longest common subsequence of two strings

HUGENUM = 2**31  # substitute for +Inf, for simplicity

def lcs(x, y):
    # step 1: init dp with tuples (+Inf, x_idx, y_idx); O(|x|*|y|)
    dp = []
    for i in range(len(x)+1):
        dpy = [(HUGENUM, 0, 0)] * (len(y)+1)
        dp.append(dpy)
    for i in range(len(x)+1):  # guard row
        dp[i][len(y)] = (len(x)-i, 0, 0)
    for j in range(len(y)+1):  # guard column
        dp[len(x)][j] = (len(y)-j, 0, 0)
    # step 2: dynamic programming on suffixes of x and y; O(|x|*|y|)
    for i in reversed(range(len(x))):
        for j in reversed(range(len(y))):
            # case 1: replacement, cost 0
            if x[i] == y[j]:
                if dp[i][j][0] > dp[i+1][j+1][0]:
                    dp[i][j] = (dp[i+1][j+1][0], i+1, j+1)
            # case 2: delete from x, cost 1
            if dp[i][j][0] > 1 + dp[i+1][j][0]:
                dp[i][j] = (1 + dp[i+1][j][0], i+1, j)
            # case 3: delete from y, cost 1
            if dp[i][j][0] > 1 + dp[i][j+1][0]:
                dp[i][j] = (1 + dp[i][j+1][0], i, j+1)
    # step 3: print out common subsequence; O(max(|x|,|y|))
    print "lcs for x=`%s` and y=`%s`:" % (x, y),
    i, j = 0, 0
    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            print x[i],
        i, j = dp[i][j][1], dp[i][j][2]
    print


def test():
    lcs("HIEROGLYPHOLOGY", "MICHAELANGELO")
    lcs("HAWKBILL THESE PROFITS", "UNSKILLED OTHER PROOF")