def helper(arr,start,end,k):
    if start >= end:
        return 0
    if arr[end] - arr[start] <=k:
        return 0

    ans1 = 1 + helper(arr,start,end-1,k)
    ans2 = 1 + helper(arr,start+1,end,k) 

    return min(ans1,ans2)




def minRemovals(arr,k):
    arr.sort()
    n = len(arr)
    end = n-1
    start = 0
    return helper(arr,start,end,k)

def helperDP(arr,start,end,k,dp):
    if start>=end:
        return 0
    if arr[end] - arr[start] <= k:
        return 0

    if dp[start][end] != -1:
        return dp[start][end]
    
    ans1 = 1+helperDP(arr,start,end-1,k,dp)
    ans2 = 1+helperDP(arr,start+1,end,k,dp)
    dp[start][end] = min(ans1,ans2)
    return dp[start][end]

def minRemovalsDP(arr,k):
    arr.sort()
    n = len(arr)
    end = n-1
    start = 0
    dp = [[-1]*n for _ in range(n)]
    return helperDP(arr,start,end,k,dp)
    

arr = [1,5,6,2,8]
k = 2
print(minRemovals(arr,k),minRemovalsDP(arr,k))