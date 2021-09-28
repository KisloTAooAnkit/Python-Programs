#https://leetcode.com/problems/longest-consecutive-sequence/
import sys
def longesConse(arr):
    n = len(arr)

    dic = dict()
    for data in arr:
        if data in dic:
            dic[data] +=1
        else:
            dic[data] =1

    ans = -sys.maxsize
    for key in dic:
        if key-1 in dic:
            continue
        count = 1
        val = key
        while(val in dic):
            dic[val] = count
            val +=1
            count+=1
    for key in dic:
        ans = max(ans,dic[key])
    return ans

nums = [0,3,7,2,5,8,4,6,0,1]

print(longesConse(nums))