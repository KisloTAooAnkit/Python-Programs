def coinChangeRecur(denom,idx,amount):
    if idx == len(denom) or amount < 0:
        return 0
    if amount == 0:
        return 1
    
    ans1 = coinChangeRecur(denom,idx,amount-denom[idx])
    ans2 = coinChangeRecur(denom,idx+1,amount)
    return ans1 + ans2

def dpSol(denom,amount,n,dp):
    if n == 0 or amount<0:
        return 0
    if amount == 0:
        return 1
    if dp[amount][n] > -1:
        return dp[amount][n]
    
    dp[amount][n] = dpSol(denom,amount-denom[n-1],n,dp) + dpSol(denom,amount,n-1,dp)
    return dp[amount][n]


def coinChange(denominations,amount):
    ans1 = coinChangeRecur(denominations,0,amount)
    dp = [[-1 for _ in range(len(denominations)+1)] for _ in range(amount +1)]
    ans2 = dpSol(denominations,amount,len(denominations),dp)
    print(ans1,ans2)
    
coins = [1,2,3]
val = 4
coinChange(coins,4)