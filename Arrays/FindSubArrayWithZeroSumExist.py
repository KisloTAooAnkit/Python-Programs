def subArrayExists(arr):
    n = len(arr)
    runningSum = 0
    hasMap = dict()
    for i in range(0,n):
        runningSum += arr[i]
        if(runningSum in hasMap):
            return "Yes"
        else:
            hasMap[runningSum] = 1
    
    return "No"

arr= [4, 2 ,-3, 1, 6]
print(subArrayExists(arr))
        