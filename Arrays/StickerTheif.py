#https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1
import sys
def FindMaxSum(a,n):
    if(n<=2):
        return max(a)
    prev2 = a[0]
    prev = a[1]
    ans = -sys.maxsize
    for i in range(2,n):
        current = max(prev,a[i]+prev2)
        ans = max(current,ans)
        prev2 = prev
        prev = current
    return ans

a = [1,2,3]
n = len(a)
print(FindMaxSum(a,n))