import sys
def maxLengthChain(arr):
    arr.sort(key = lambda x : x[1])
    ans = 0
    n = len(arr)
    endTime = -sys.maxsize
    for i in range(n):
        if arr[i][0]>endTime:
            ans+=1
            endTime = arr[i][1]
    return ans