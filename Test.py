import sys
from bisect import bisect_left,bisect_right
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

def lengthOfLIS1(arr,count) -> int:
    dp = []
    n = 0
    x = 0
    for i in range(count):
        if n == 0:
            dp.append(arr[i])
            x+=1
            n+=1
            continue
        val = bisect_right(dp,arr[i]) #binSearch(dp,n,arr[i])
        if val >= n:
            dp.append(arr[i])
            n+=1
            x+=1
        elif dp[val] == arr[i]:
            #x+=1
            pass
        else:
            dp[val] = arr[i]
    return x
def lengthOfLIS(arr,count) -> int:
    n = count
    dp = [0]*n
    dp[0] = 1
    for i in range(1,n):
        val = arr[i]
        dp[i] = 1
        for j in range(i-1,-1,-1):
            if arr[j] <= val:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)
def sol(arr,k):
    count = 0
    n = len(arr)
    dp = [False]*n
    for i in range(n):
        if dp[i]:
            continue
        j = i
        a = []
        c = 0
        while(j<n):
            a.append(arr[j])
            dp[j] = True
            c+=1
            j+=k
        ans = lengthOfLIS1(a,c)
        count += c-ans

    return count          
        

# arr=[4,1,5,2,6,2]
# k =2   
arr =[12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
k = 1
print(sol(arr,k))

def sol(logs,n):
    stack = []
    ans = [0]*n
    lastExeTime = -1
    for log in logs:
        id,action,time = log.split(":")
        if action == "start":
            if stack:
                ans[-1] += int(time) - lastExeTime
            stack.append([int(id)])
            
    return ans

n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(sol(logs,n))
