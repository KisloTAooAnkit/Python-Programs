import sys
def check(arr,target,childCount,n):
    
    maxsum = 0
    runningsum = 0
    for i in range(n-1,target-2,-1):
        runningsum +=arr[i]
        if(runningsum>target):
            maxsum = max(runningsum,maxsum)
            runningsum = 0
            target-=1
    
    return maxsum


def allocatePages(arr,childCount):
    end = sum(arr)
    start = 0
    ans = sys.maxsize
    n = len(arr)
    while(start<=end):
        mid = start + (end-start)//2
        val = check(arr,mid,childCount,n)
        ans = min(ans,val)
        if(mid>arr[-1]):
            end = mid-1
        else:
            start = mid+1
    
    return ans