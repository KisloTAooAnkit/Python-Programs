import bisect

def maxPairSum(arr,k):
    n = len(arr)
    arr.sort()
    arr = arr[::-1]

    ans = 0
    lastMarkedIdx = -1
    for i in range(n-1):
        if i == lastMarkedIdx:
            continue
        if arr[i] - arr[i+1] < k:
            ans += arr[i] + arr[i+1]
            lastMarkedIdx = i+1
    return ans

k = 12
arr = [5, 15, 10, 300]
print(maxPairSum(arr,k))