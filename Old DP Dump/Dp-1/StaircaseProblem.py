def stairCase(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    if(n==2):
        return 2
    
    ansn_1 = stairCase(n-1)
    ansN_2 = stairCase(n-2)
    ansN_3 = stairCase(n-3)
    return ansn_1 + ansN_2 + ansN_3


def stairCaseDP(n,dp):
    if(n==0):
        return 1
    if(n==1):
        return 1
    if(n==2):
        return 2
    if(dp[n]>0):
        return dp[n]
    ans = stairCase(n-1) + stairCase(n-2) + stairCase(n-3)
    dp[n] =ans
    return ans

n=4
dp = [0]*(n+1) 


def stairCase_i(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3,(n+1)):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

print(stairCase_i(n))