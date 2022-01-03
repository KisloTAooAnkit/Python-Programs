def wiggle(arr):
    n = len(arr)
    dp = [[1]*n for _ in range(2)]
    dp[0][0] = 1
    dp[1][0] = 1
    ans = 1
    for i in range(1,n):

        #gadha
        for j in range(i-1,-1,-1):
            if arr[j] > arr[i]:
                dp[1][i] = max(dp[1][i],dp[0][j] +1)
                ans = max(dp[1][i],ans)
        for j in range(i-1,-1,-1):
            if arr[j] < arr[i]:
                dp[0][i] = max(dp[0][i],dp[1][j]+1)
                ans = max(dp[0][i],ans)
    return ans


arr = [1,17,5,10,13,15,10,5,16,8]
print(wiggle(arr))