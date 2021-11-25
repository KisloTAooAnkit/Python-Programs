

def helper(arr,n,idx,cd):
    if n==0:
        return 0
    ans2 =0
    if cd < 3:
        ans2 = arr[idx] + helper(arr,n-1,idx+1,cd+1)
    ans1 = helper(arr,n-1,idx+1,1)
    return max(ans1,ans2)

def solution(arr):
    n = len(arr)
    return helper(arr,n,0,1)

def helperDp(arr,n,idx,cd,dp):
    if n==0:
        return 0
    if dp[cd][n]>-1:
        return dp[cd][n]
    ans2 = 0
    if cd<3:
        ans2 = arr[idx] + helperDp(arr,n-1,idx+1,cd+1,dp)
    ans1 = helperDp(arr,n-1,idx+1,1,dp)
    dp[cd][n] = max(ans1,ans2)
    return dp[cd][n]

def solutionDp(arr):
    n = len(arr)
    dp = [[-1 for _ in range(n+1)] for _ in range(4)]
    return helperDp(arr,n,0,1,dp)


arr = [3000, 2000, 1000, 3, 10]

print(solution(arr),solutionDp(arr))