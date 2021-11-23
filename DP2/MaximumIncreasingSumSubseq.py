def maxSum(arr):
    n = len(arr)
    dp = [0]*n
    dp[0] = arr[0]
    for i in range(1,n):
        ans = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] < arr[i]:
                ans = max(ans,dp[j]+arr[i])
        dp[i] = ans
    
    
    return max(dp) 


arr = [44,42,38,21,15,22,13,27]
print(maxSum(arr))