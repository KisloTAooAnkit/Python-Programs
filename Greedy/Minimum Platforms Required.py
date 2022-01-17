from platform import platform


def minPlatforms(arr,dep):
    arr.sort()
    dep.sort()
    
    n = len(arr)
    i = 0
    j = 0
    runningPlatformCount = 0
    maxPlatforms = 0
    while(i<n and j<n):
        if arr[i] <= dep[j]:
            i+=1
            runningPlatformCount +=1
            maxPlatforms = max(maxPlatforms,runningPlatformCount)
        else:
            j+=1
            runningPlatformCount -=1
    return maxPlatforms


def minPlatformsRQ(arr,dep):
    
    diffArray = [0]*2402    
    n = len(arr)
    for i in range(n):
        diffArray[arr[i]] +=1
        diffArray[dep[i]+1] -=1
    ans = 0
    for i in range(2402):
        if i == 0:
            continue
        diffArray[i] += diffArray[i-1]
        ans = max(ans,diffArray[i])
    return ans
        