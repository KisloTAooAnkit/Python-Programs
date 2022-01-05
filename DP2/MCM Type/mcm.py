def mcm(arr,i,j):
    
    if i >=j:
        return 0
    
    minAns = float("inf")
    
    for k in range(i,j):    
        
        ans = mcm(arr,i,k) + (arr[i-1] *arr[k]*arr[j] ) + mcm(arr,k+1,j)
        minAns = min(minAns,ans)
    return minAns 


def mcmDP(arr,i,j,dp):
    
    if i >= j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    minAns = float("inf")
    for k in range(i,j):
        
        ans = mcmDP(arr,i,k,dp) + (arr[i-1] *arr[k]*arr[j] ) + mcmDP(arr,k+1,j,dp)
        minAns = min(minAns,ans)
    dp[i][j] = minAns
    return minAns 


arr = [1, 2, 3, 4, 3]
n = len(arr)
dp = [[-1]*n for _ in range(n+1)]

print(mcmDP(arr,1,len(arr)-1,dp))