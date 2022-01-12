

def longestSubarrayWithAtMostKSum(arr,k):
    n = len(arr)
    suffix = [0]*n

    sm = 0
    for i in range(n-1,-1,-1):
        suffix[i] = sm
        sm = min(0,sm+arr[i])
    ans = float("-inf")
    runningSum = 0
    start = 0
    end = 0
    
    while(end<n):
        runningSum += arr[end]
        while(start<=end and runningSum+suffix[end]>k):
            runningSum -= arr[start]
            start +=1   
        ans = max(runningSum,ans)
        end +=1
    return ans

arr = [-5, 8, -14, 2, 4, 12] 
k = 5

print(longestSubarrayWithAtMostKSum(arr,k))
