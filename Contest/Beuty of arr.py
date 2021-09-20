from typing import AnyStr


def NSR(arr,twoRes):
    stack = []
    n = len(arr)
    for i in range(0,n):
        while(stack and arr[stack[-1]]>=arr[i]):
            idx = stack.pop(-1)
            twoRes[idx] = twoRes[idx] and False 
        stack.append(i)
    return twoRes
def NGL(arr,twoRes):
    stack = []
    n = len(arr)
    for i in range(n-1,-1,-1):
        while(stack and arr[stack[-1]]<=arr[i]):
            idx = stack.pop()
            twoRes[idx] = twoRes[idx] and False
        stack.append(i)
    return twoRes

def sumofBooty(arr):
    n = len(arr)
    twoRes = [True]*n
    twoRes =NGL(arr,twoRes)
    twoRes = NSR(arr,twoRes)
    maxprofit = 0
    for i in range(1,n-1):
        if twoRes[i]:
            maxprofit +=2
            continue
        elif arr[i - 1] < arr[i] and arr[i] < arr[i + 1]:
            maxprofit +=1
    return maxprofit
        
        

a = [3,2,1]
print(sumofBooty(a))
