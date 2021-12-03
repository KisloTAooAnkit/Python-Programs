def helper(n,idx,arr,lhs,rhs):
    if lhs == rhs:
        return True
    if n== 0:
        return False

    ans1 = helper(n-1,idx+1,arr,lhs+arr[idx],rhs-arr[idx])
    ans2 = helper(n-1,idx+1,arr,lhs,rhs)
    return ans1 or ans2

def helperDP(n,idx,arr,lhs,rhs,dp,flag):
    if flag[0]:
        return True
    if lhs == rhs:
        flag[0] = True
        return True
    if n== 0:
        return False

    if dp[n][rhs] != -1:
        return dp[n][rhs] == 1

    ans1 = helperDP(n-1,idx+1,arr,lhs+arr[idx],rhs-arr[idx],dp,flag)
    ans2 = helperDP(n-1,idx+1,arr,lhs,rhs,dp,flag)
    dp[n][rhs] = 1 if ans1 or ans2 else 0
    return dp[n][rhs] == 1

def partition(arr):
    s = sum(arr)
    n = len(arr)
    dp = [[-1]*(s+1) for _ in range(n+1)]
    flag = [False]
    return helperDP(n,0,arr,0,s,dp)

arr = [1,2,3,5]
print(partition(arr))