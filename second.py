
from bisect import bisect_left

def sol(arr1,arr2):
    n = len(arr1)
    ans = 0
    for i in range(n):
        ans += abs(arr1[i] - arr2[i])
    res = arr1[:]
    arr1.sort()
    temp = ans
    for i in range(n):
        idx = bisect_left(arr1,arr2[i])
        prev = idx-1
        nxt = idx +1
        val = float("inf")
        if prev >-1:
            val = min(val,abs(arr1[prev]-arr2[i]))
        if nxt < n:
            val = min(val,abs(arr1[nxt]-arr2[i]))
        val = min(val,abs(arr1[idx]-arr2[i]))
        
        val = val - abs(res[i]-arr2[i])
        temp = min(temp,ans+val)
    return temp            
    
n1 = [1,10,4,4,2,7]
n2 = [9,3,5,1,7,4]

print(sol(n1,n2))