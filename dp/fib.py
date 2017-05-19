# dynamic programming: fibonacci

# naive, O(2^f)
def naive(f):
    if f == 1 or f == 2:
        return 1
    return naive(f-1) + naive(f-2)

# top-down (recursive), #subproblems = O(f), #choices = O(1), time = O(f)
def dp1(f):
    dp = [0] * f
    dp[0] = 1; dp[1] = 1
    return dp1recurse(dp, f-1)

def dp1recurse(dp, f):
    if dp[f] > 0:
        return dp[f]
    res = dp1recurse(dp, f-1) + dp1recurse(dp, f-2)
    dp[f] = res
    return res

# bottom-up (topological order), time = O(f)
def dp2(f):
    dp = [0] * f
    dp[0] = 1; dp[1] = 1
    for i in range(2, f):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[f-1]


def test():
    print "fib(10) =", dp1(10), "fib(50) =", dp1(50)
    print "fib(10) =", dp2(10), "fib(50) =", dp2(50)    