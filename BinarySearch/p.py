import sys
arr = [1,2,3,4,5,6,7,8]
n = len(arr)
target = 18
childCount = 3
runningsum = 0
maxsum = 0
for i in range(n-1 , childCount -2,-1):
    runningsum += arr[i]
    if(runningsum>target):
        print(runningsum)
        childCount-=1
        runningsum =0