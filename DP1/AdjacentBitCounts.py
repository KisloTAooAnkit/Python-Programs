def adjcHelper(first,n,k):    
    if (n==1):
        if k==0:
            return 1
        return 0
    if k<0:
        return 0 
    
    ans = 0
    if first == 1:
        ans = adjcHelper(1,n-1,k-1) + adjcHelper(0,n-1,k)
    elif first == 0:
        ans = adjcHelper(1,n-1,k) + adjcHelper(0,n-1,k)
    return ans

def adjcHelperDp(first,n,k,dp):
    if (n==1):
        if k==0:
            return 1
        return 0
    if k<0:
        return 0 
    if dp[first][n][k] > -1:
        return dp[first][n][k]
    ans = 0
    if first == 1:
        ans = adjcHelperDp(1,n-1,k-1,dp) + adjcHelperDp(0,n-1,k,dp)
    elif first == 0:
        ans = adjcHelperDp(1,n-1,k,dp) + adjcHelperDp(0,n-1,k,dp)
    dp[first][n][k] = ans
    return ans


def caller(n,k):
    dp = [[[-1 for _ in range(k+1)] for _ in range(n+1)] for _ in range(2)]
    ans = adjcHelperDp(0,n,k,dp) + adjcHelperDp(1,n,k,dp)
    return ans

n= 30
k = 17
print(caller(n,k))
