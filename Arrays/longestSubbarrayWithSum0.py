def longestSubarrWithSum0(arr):
    runningSum = 0
    ans = 0
    dic = {0:0}
    n = len(arr)
    for i in range(n):
        runningSum += arr[i]
        if runningSum not in dic:
            dic[runningSum]  = i
            continue
        start = dic[runningSum]
        end = i
        ans = max(ans,end-start)
    return ans

a = [15,-2,2,-8,1,7,10,23]
print(longestSubarrWithSum0(a))