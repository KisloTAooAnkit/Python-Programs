def helper(n):
    if n == 0:
        return 1
    if n== 1:
        return 1
    ans = 0
    for i in range(0,n):
        left = helper(i)  
        right = helper(n-1-i)
        val = left*right
        ans = ans + val
    return ans

def CountBSTDp(n,dp):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if dp[n] > -1:
        return dp[n]
    ans = 0
    for i in range(0,n):
        left = CountBSTDp(i,dp)
        right = CountBSTDp(n-1-i,dp)
        val = left*right
        ans += val
    dp[n] = ans
    return dp[n]

def CountBSTIterative(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        for j in range(0,i):
            left = dp[j]
            right = dp[i-1-j]
            dp[i] += (left*right)
    return dp[n]

def countBST(n):
    dp = [-1 for _ in range(n+1)]
    ans = CountBSTDp(n,dp)
    ans = CountBSTIterative(n)
    return ans% ((10**9) + 7)
print(countBST(3))