def findPairs(arr,k):
    n = len(arr)
    ans = 0
    for i in range(n-1):
        val1 = arr[i]
        for j in range(i+1,n):
            if abs(val1 - arr[j]) == k:
                ans +=1
    return ans


a = [1,2,2,1]
k = 1
print(findPairs(a,k))
    