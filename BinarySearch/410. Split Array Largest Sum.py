from typing import List
def isValid(target,arr,slots,ans):
    reqSlots = 1
    runningSum = arr[0]
    maxSumperSlot  = 0
    for i in range(1,len(arr)):
        if runningSum >= target:
            reqSlots += 1
            maxSumperSlot = max(runningSum,maxSumperSlot)
            runningSum = arr[i]
        else:
            runningSum += arr[i]
    if slots == reqSlots:
        ans[0] = min(ans[0],maxSumperSlot)
    return reqSlots
        


def splitArray(arr: List[int], m: int) -> int:
    end = sum(arr)
    start = 0
    ans = [float("inf")]
    while(start<=end):
        mid = (end+start)//2
        
        res = isValid(mid,arr,m,ans)
        if(res == m):
            end = mid - 1
        elif res > m:
            start = mid + 1
        else:
            end = mid - 1
    return ans[0]


arr = [7,2,5,10,8]
t = 2
print(splitArray(arr,t))