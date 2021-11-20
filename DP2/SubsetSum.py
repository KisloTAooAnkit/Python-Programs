def helper(arr,target,n,idx):
    if target <0:
        return 0
    if target == 0:
        return 1
    if n<=0:
        return 0

    ans1 = helper(arr,target-arr[idx],n-1,idx+1)
    ans2 = helper(arr,target,n-1,idx+1)
    return max(ans1,ans2)    

def helperDP(arr,target,n,idx,dp):
    if target <0:
        return 0
    if target == 0:
        return 1
    if n<=0:
        return 0
    if dp[target][n] > -1:
        return dp[target][n]
    ans1 = helperDP(arr,target-arr[idx],n-1,idx+1,dp)
    ans2 = helperDP(arr,target,n-1,idx+1,dp)
    dp[target][n] = max(ans1,ans2) 
    return dp[target][n] 

def solve(a,b):
    n = len(a)
    dp = [[-1 for _ in range(n+1)] for _ in range(b+1)]
    return helperDP(a,b,n,0,dp)

a = [3, 34, 4, 12, 5, 2]
b = 9
print(solve(a,b))