from bisect import bisect_right as upper_bound
from typing import Mapping

def minRemovals(arr,k):
    ans = float("inf")
    arr.sort()
    n = len(arr)
    for i in range(0,n):
        idx = upper_bound(arr,k+arr[i],i+1,n)
        ans = min(ans,n-idx + i)
    return ans

arr = [1,3,4,9,10,11,12,17,20]
k = 4
print(minRemovals(arr,k))