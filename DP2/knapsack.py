def helper(capacity,wtarr,valarr,idx,n):
    
    if capacity <= 0:
        return 0
    
    if n <= 0:
        return 0
    ans1 = 0
    if wtarr[idx] <= capacity:
        ans1 = valarr[idx] + helper(capacity-wtarr[idx],
                                    wtarr,
                                    valarr,
                                    idx+1,
                                    n-1)
    
    ans2 = helper(capacity,wtarr,valarr,idx+1,n-1)
    return max(ans2,ans1)

def knapSack(capacity, wtarr, valarr, n):
    return helper(capacity,wtarr,valarr,0,n)

#DP
def helperDP(capacity,wtarr,valarr,idx,n,dp):
    if capacity <= 0:
        return 0
    
    if n <= 0:
        return 0
    if dp[capacity][n] > -1:
        return dp[capacity][n]
    ans1 = 0
    if wtarr[idx] <= capacity:
        ans1 = valarr[idx] + helperDP(capacity-wtarr[idx],
                                    wtarr,
                                    valarr,
                                    idx+1,
                                    n-1,
                                    dp)
    
    ans2 = helperDP(capacity,wtarr,valarr,idx+1,n-1,dp)
    dp[capacity][n] = max(ans2,ans1)
    return  dp[capacity][n]

def knapSackDP(capacity, wtarr, valarr, n):
    dp = [[-1 for _ in range(n+1)] for _ in range(capacity+1)]
    return helperDP(capacity,wtarr,valarr,0,n,dp)

def knapSackIter(capacity,wtarr,valarr,n):
        dp = [[0 for _ in range(n+1)] for _ in range(capacity+1)]
        for i in range(1,capacity+1):
            for j in range(1,n+1):
                ans1 = 0
                remainingCapacity = i - wtarr[n-j]
                if remainingCapacity >= 0:
                    ans1 = valarr[n-j] + dp[remainingCapacity][j-1]
                ans2 = dp[i][j-1]
                dp[i][j] = max(ans1,ans2)
        return dp[capacity][n]
n = 3
w = 4
val = [1,2,3]
wt = [4,5,1]
print(knapSackIter(w,wt,val,n))