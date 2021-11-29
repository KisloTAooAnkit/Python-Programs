def minJumpsGreedy(arr):
    n = len(arr)
    if n==1:
        return 0
    i = 0
    ans = 0
    while(i<n-1):
        if arr[i] == 0:
            return -1
        start = i+1
        end = i + arr[i] if i + arr[i]<n-1 else n-1
        mx = float("-inf")
        for j in range(start,end+1):
            val = j + arr[j]
            val = val if val<n-1 else n-1
            if mx<=arr[j]:
                i = j
                mx = arr[j]
        ans +=1
    return ans

def minJumpsDP(arr):
    n = len(arr)
    dp = [float("inf")]*n
    if n==1:
        return 0
    for i in range(n-1,-1,-1):
        if i + arr[i] >= n-1:
            dp[i] = 1
            continue
        for j in range(i+1,i+arr[i]+1):
            dp[i] = min(dp[i],dp[j]+1)
    return dp[0]

arr = [3,2,1]
print(minJumpsDP(arr),minJumpsGreedy(arr))
    
