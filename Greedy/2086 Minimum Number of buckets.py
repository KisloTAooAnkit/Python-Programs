def minBuckets(arr):
    n = len(arr)
    dp = [0]*n
    if n==1 and arr[0] == "H":
        return -1
    if n >= 2:
        if arr[0] == "H" and arr[1] == "H":
            return -1
        if arr[n-1] == "H" and arr[n-2] == "H":
            return -1
    contHCount = 0
    for i in arr:
        if contHCount == 3:
            return -1
        if i == "H":
            contHCount +=1
        if i == ".":
            contHCount = 0

    for i in range(n):
        if arr[i] == "H":
            if i+1 <n and arr[i+1] != "H":
                dp[i+1] = 1
    for i in range(n-1,-1,-1):
        if arr[i] == "H":
            if i+1<n and dp[i+1] ==2:
                continue
            #greedy choice point
            if i-1>=0:
                dp[i-1] +=1
                if i+1<n:
                    dp[i+1] -=1
    
    buckets = 0
    for i in range(n):
        if dp[i] >0:
            buckets +=1
    return buckets

s = ".H.H."
print(minBuckets(s))