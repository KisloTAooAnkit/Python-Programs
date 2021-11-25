def findLongest(arr):
    arr.sort()
    n = len(arr)
    dp = [0]*n
    dp[0] = 1
    for i in range(1,n):
        runningMax = 1
        curr = arr[i]
        for j in range(i-1,-1,-1):
            prev = arr[j]
            if prev[1] < curr[0]:
                runningMax = max(runningMax,1+dp[j])
        dp[i] = runningMax
    return max(dp)


a = [[1,2],[2,3],[3,4]]
print(findLongest(a))