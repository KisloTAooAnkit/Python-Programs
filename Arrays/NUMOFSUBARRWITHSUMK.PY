def subarraySum(arr,k):
    dic = {0:1}
    runningSum = 0
    ans = 0
    for i in range(0,len(arr)):
        runningSum += arr[i]
        redundantSum = runningSum - k
        ans += dic.get(redundantSum,0)
        if runningSum in dic:
            dic[runningSum] +=1
        else:
            dic[runningSum] = 1
    return ans

nums = [1,2,3] 
k = 3
print(subarraySum(nums,k))