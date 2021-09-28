#https://leetcode.com/problems/sum-of-subarray-minimums/
import sys
def NSR(arr,temp,n):
    stack=[]
    for i in range(0,n):
        while(stack and arr[stack[-1]]>arr[i]):
            idx = stack.pop(-1)
            temp[idx] *= (abs(idx-i))
        stack.append(i)
def NSL(arr,temp,n):
    stack=[]
    for i in range(n-1,-1,-1):
        while(stack and arr[stack[-1]]>=arr[i]):
            idx = stack.pop(-1)
            temp[idx] *= (abs(idx-i))
        stack.append(i)



def sumSubarrayMins(arr):
    arr = [-sys.maxsize]+arr+[-sys.maxsize]
    n = len(arr)
    temp = [1]*n
    NSR(arr,temp,n)
    NSL(arr,temp,n)
    ans = 0
    for i in range(1,n-1):
        ans += temp[i] * arr[i]
    return ans

arr= [71,55,82,55]

print(sumSubarrayMins(arr))