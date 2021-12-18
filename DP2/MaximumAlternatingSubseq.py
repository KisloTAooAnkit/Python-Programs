
def dfs(arr,i,n,mode):
    if n == 0:
        return 0
    #true = add
    #false = subtract
    ans1 = float("-inf")
    if mode:
        ans1 = arr[i] + dfs(arr,i+1,n-1,not mode)
    else:
        ans1 = -arr[i] + dfs(arr,i+1,n-1,not mode)
    ans2 = dfs(arr,i+1,n-1,mode)
    return max(ans1,ans2)

def dfsDP(arr,i,n,mode,dp):
    if n==0:
        return 0
    
    if dp[n][mode] != -1:
        return dp[n][mode]
    
    ans1 = float("-inf")
    if mode == 1:
        ans1 = arr[i] + dfsDP(arr,i+1,n-1,1-mode,dp)
    else:
        ans1 = -arr[i] + dfsDP(arr,i+1,n-1,1-mode,dp)
    ans2 = dfsDP(arr,i+1,n-1,mode,dp)
    dp[n][mode] = max(ans1,ans2)
    return dp[n][mode] 

def solution(arr):
    return dfs(arr,0,len(arr),True)
def dpSol(arr):
    n = len(arr)
    dp = [[-1]*2 for _ in range(n+1)]
    return dfsDP(arr,0,n,1,dp)
arr = [1,2,3,8]
print(dpSol(arr))