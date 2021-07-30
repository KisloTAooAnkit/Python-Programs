def MaxLenOfK(arr,k):
    start = 0
    end = start+k
    n = len(arr)
    maxsum = sum(arr[start:k])
    runningSum = maxsum
    for i in range(1,n):
        start = i
        end = start+k-1
        if end >= n:
            break

        runningSum = runningSum - arr[i-1] + arr[end]
        maxsum = max(runningSum,maxsum)
    return maxsum 
    
arr = [2,5,1,8,2,9,1]
k = 3

print(MaxLenOfK(arr,k))