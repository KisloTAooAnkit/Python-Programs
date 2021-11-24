def longestSubseqWithAdjacent1Diff(arr):
    n = len(arr)
    dp = [1]*n
    dp[0] = 1
    for i in range(1,n):
        current_max = 1
        for j in range(i-1,-1,-1):
            if abs(arr[j] - arr[i]) == 1:
                current_max = max(current_max , 1 + dp[j])
        dp[i] = current_max
    return max(current_max)