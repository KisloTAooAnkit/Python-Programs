def helper(n,arr,idx):
    if n== 0:
        return 1
    if n<0 or idx >=len(arr):
        return 0
    
    ans1 = helper(n-arr[idx],arr,idx)
    ans2 = helper(n,arr,idx+1)
    return ans1 + ans2

def count(n):
    arr = [3,5,10]
    print(helper(n,arr,0))

def helperDP(n,arr,idx,ln,dp):
    if n ==0:
        return 1
    if n<0 or ln <=0:
        return 0
    
    if dp[n][ln] != -1:
        return dp[n][ln]
    
    ans1 = helperDP(n-arr[idx],arr,idx,ln,dp)
    ans2 = helperDP(n,arr,idx+1,ln-1,dp)
    dp[n][ln] = ans1 + ans2
    return dp[n][ln]

def countDP(x):
    arr = [3,5,10]
    dp = [[-1 for _ in range(4)]for _ in range(x+1)]
    print(helperDP(x,arr,0,3,dp))
    

x = 20
countDP(x)