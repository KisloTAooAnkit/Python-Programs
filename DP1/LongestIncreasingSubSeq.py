

def LIS(arr):
    n = len(arr)
    dp = [0]*n
    dp[0] = 1
    for i in range(1,n):
        val = arr[i]
        dp[i] = 1
        for j in range(i-1,-1,-1):
            if arr[j] < val:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

def binSearch(dp,n,val):
    start = 0
    end = n-1
    ans = -1
    while(start<=end):
        mid = (start+end)//2
        if dp[mid] >= val:
            ans = mid
            end = mid-1
        elif dp[mid] < val:
            start = mid +1
    return ans

def LIS_NLOGN(arr):
    dp = []
    n = 0
    for i in range(len(arr)):
        if n == 0:
            dp.append(arr[i])
            n+=1
            continue
        val = binSearch(dp,n,arr[i])
        if val == -1:
            dp.append(arr[i])
            n+=1
        else:
            dp[val] = arr[i]
    return n
        

arr = [0,1,0,3,2,3]
print(LIS_NLOGN(arr))