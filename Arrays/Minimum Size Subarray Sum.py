#https://leetcode.com/problems/minimum-size-subarray-sum/
def minSubArrayLen(target,arr):
    n = len(arr)
    minLen = n
    runningLen = 0
    runningsum = 0
    start = 0
    end = 0

    if(sum(arr)<target):
        return 0

    while(end<n):
        runningsum+=arr[end]
        runningLen +=1
        while(runningsum>=target):
            minLen = min(runningLen,minLen)
            runningsum -= arr[start]
            runningLen -= 1
            start+=1
        

        end+=1
    
    return minLen


target = 11
nums = [1,1,1,1,1,1,1,1]
print(minSubArrayLen(target,nums))
