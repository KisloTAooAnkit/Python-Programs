def fib(n):
    if(n==0 or n==1):
        return 1
    
    return fib(n-1) + fib(n-2)

def fibDP(n,arr):
    if(n==0 or n==1):
        arr[n] = n
        return n
    if(arr[n]>0):
        return arr[n]
    else:
        ans = fibDP(n-1,arr)+fibDP(n-2,arr)
        arr[n] = ans
    return arr[n]

n=9
arr=[0]*(n+1)
print(fibDP(n,arr))