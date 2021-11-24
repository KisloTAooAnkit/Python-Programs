def subArraySumLessThanK(arr,k):
    if k <=0:
        return 0
    runningSum = 0
    start = 0
    end = 0
    n = len(arr)
    ans = 0
    while(end<n):
        runningSum += arr[start]
        while(runningSum>=k):
            k-=arr[start]
            start+=1
        ans += end - start +1
        end+=1

        