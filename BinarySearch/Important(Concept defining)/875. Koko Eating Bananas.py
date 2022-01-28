import math
def isPossible(arr,perHour,target):
    reqHours = 0
    for i in arr:
        reqHours += math.ceil(i/perHour)
    return reqHours <= target 


def kokoBananas(arr,k):
    start = 0
    end = sum(arr)
    ans = -1
    while(start<=end):
        mid = start + (end-start)//2
        if isPossible(arr,mid,k):
            end = mid-1
            ans = mid
        else:
            start = mid+1
    return ans

piles = [2,2]

h = 2
print(kokoBananas(piles,h))