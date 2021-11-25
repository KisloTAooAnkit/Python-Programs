from typing import AnyStr


def minJumpsGreedy(arr):
    
    jumpCount = 0
    i =0
    n = len(arr)
    while(i<n-1):
        currmax = 0
        idx = 0
        if arr[i] == 0:
            return -1
        dest = n-1 if i + arr[i] >=n-1 else i + arr[i]
        for j in range(i+1,dest+1):
            if arr[j] > currmax:
                currmax = arr[j]
                idx = j
        jumpCount +=1
        i = idx
    return jumpCount

def minJumpsDP(arr):
    n = len(arr)
    dp = [float("inf")]*n
    for i in range(n-1,-1,-1):
        if i + arr[i] >= n-1:
            dp[i] = 1
            continue
        for j in range(i+1,i+arr[i]+1):
            dp[i] = min(dp[i],dp[j]+1)
    return dp[0]

arr = [1,3,5,8,9,2,6,7,6,8,9]
print(minJumpsDP(arr))
    
