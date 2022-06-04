from bisect import bisect_left

def solve(arr):
    n = len(arr)
    dp = [arr[0]]
    for i in range(1,n):
        idx = bisect_left(dp,arr[i])
        if idx >= len(dp):
            dp.append(arr[i])
        else:
            dp[idx] = arr[i]
    return len(dp)
arr = [2,5,3,7,11,8,10,13,6]
print(solve(arr))