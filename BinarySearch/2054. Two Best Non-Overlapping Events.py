def maxTwoEvents(arr):
    arr.sort()
 
    n  = len(arr)
    maxProfitTillNowR2L = [0]*n
    for i in range(n-1,-1,-1):
        if i == n-1:
            maxProfitTillNowR2L[i] = arr[i][2]
        else:
            maxProfitTillNowR2L[i] = max(arr[i][2],maxProfitTillNowR2L[i+1])

    maxSum = 0
    for i in range(n):
        firstInterval = arr[i]
        start = i+1
        end = n-1
        while(start<=end):
            mid = (start+end)//2
            if arr[mid][0] > firstInterval[1]:
                maxSum = max(maxSum,firstInterval[2]+maxProfitTillNowR2L[mid])
                end = mid-1
            else:
                start = mid+1
        if start > end:
            maxSum = max(maxSum,firstInterval[2])

    return maxSum

arr = [[1,5,3],[1,5,1],[6,6,5]]
print(maxTwoEvents(arr))
