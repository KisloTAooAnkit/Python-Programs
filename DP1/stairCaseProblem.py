def stairCase(n):
    if n==0:
        return 1
    if n== 1:
        return 1
    if n==2:
        return 2
    
    ans1 = stairCase(n-1)
    ans2 = stairCase(n-2)
    ans3 = stairCase(n-3)
    return ans1 + ans2 + ans3

def stairCaseDP(dp,n):
    if n==0:
        return 1
    if n== 1:
        return 1
    if n==2:
        return 2
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = stairCaseDP(dp,n-1) + stairCaseDP(dp,n-2) + stairCaseDP(dp,n-3)
    return dp[n]
def stairCaseIter(n):
    dp = [-1] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    return dp[n]
    
n =4
dp = [-1]* (n+1) 
dp[0] = 1
dp[1] = 1
dp[2] = 2
print(stairCaseDP(dp,n))
print(stairCaseIter(n))