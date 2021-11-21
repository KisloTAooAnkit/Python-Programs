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

def subsetSumIterative(arr,target):
    n = len(arr)
    dp = [[0 for i in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1,n+1):
        for j in range(1,target+1):
            ans1 = 0
            if arr[n-i] <= j:
                ans1 = dp[i-1][j-arr[n-i]]
            ans2 = dp[i-1][j]
            
            dp[i][j] = max(ans1,ans2)
    return dp[n][target]

def subsetSumWithIterativeWithSmallerSpace(arr,target):
    n = len(arr)
    dp = [[0 for i in range(target+1)] for _ in range(2)]
    dp[0][0] = 1
    dp[1][0] = 1
    flag = 1
    for i in range(1,n+1):
        for j in range(1,target+1):
            ans1 = 0
            if arr[n-i] <= j:
                ans1 = dp[flag^1][j-arr[n-i]]
            ans2 = dp[flag^1][j]
            
            dp[i][j] = max(ans1,ans2)
        flag = 1-flag # flag = flag^1
    return dp[flag^1][target]
    

a = [3, 34, 4, 12, 5, 2]
b = 37
print(solve(a,b),subsetSumIterative(a,b))