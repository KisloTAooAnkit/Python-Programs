import sys
from bisect import bisect_left,bisect_right

#LIS Patience Sort concept used 

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