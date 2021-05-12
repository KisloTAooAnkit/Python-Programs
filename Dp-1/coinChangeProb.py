def coinChange(coins,sum):
    if(sum == 0):
        return 1
    
    if(sum<0):
        return 0
    
    if(len(coins) == 0):
        return 0
    
    res1 = coinChange(coins,sum-coins[0])
    res2 = coinChange(coins[1:],sum)
    return res1 + res2


def coinChangeDP(coins,sum,dp):
    if(sum == 0):
        return 1
    
    if(sum<0):
        return 0
    
    if(len(coins) == 0):
        return 0
    
    if(dp[sum][len(coins)] > -1):
        return dp[sum][len(coins)]
    
    res1 = coinChange(coins,sum-coins[0])
    res2 = coinChange(coins[1:],sum)
    dp[sum][len(coins)] = res1 + res2
    return res1 + res2


def Caller(n,denom):
    dp = [[-1 for j in range(len(denom)+1)] for i in range(n+1)]
    print(dp)
    return coinChangeDP(denom,n,dp)


denom = [1,2,3]
val = 4
print(Caller(val,denom))