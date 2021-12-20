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

def NGR(arr,temp,n):
    stack = []
    for i in range(0,n):
        while(stack and arr[stack[-1]]<arr[i]):
            idx = stack.pop(-1)
            temp[idx] *= (abs(idx-i))
        stack.append(i)


def NGL(arr,temp,n):
    stack=[]
    for i in range(n-1,-1,-1):
        while(stack and arr[stack[-1]]<=arr[i]):
            idx = stack.pop(-1)
            temp[idx] *= (abs(idx-i))
        stack.append(i)

def sumSubarrayMins(arr):
    arr1 = [sys.maxsize] + arr + [sys.maxsize]
    arr = [-sys.maxsize]+arr+[-sys.maxsize]
    n = len(arr)
    temp1 = [1]*n
    temp2 = [1]*n
    NSR(arr,temp1,n)
    NSL(arr,temp1,n)
    NGR(arr1,temp2,n)
    NGL(arr1,temp2,n)    
    ans = 0
    for i in range(1,n-1):
        ans += (temp2[i]*arr[i])  -  (temp1[i] * arr[i])
    return ans

arr= [1,3,3]

print(sumSubarrayMins(arr))