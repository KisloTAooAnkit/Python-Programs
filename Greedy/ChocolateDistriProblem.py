def minDiff(arr,m):
    n = len(arr)
    i = m-1
    arr.sort()
    ans = float("inf")
    while(i<n):
        ans = min(ans,arr[i] - arr[i-(m-1)])
        i+=1
    return ans


arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(minDiff(arr,m))
