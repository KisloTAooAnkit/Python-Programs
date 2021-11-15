

def countArray(k,x,n):
    a = [0]*n
    b = [0]*n
    a[0] = 1 if x== 1 else 0
    b[0] = 0 if x==1 else 1
    for i in range(1,n):
        a[i] = b[i-1]
        b[i] = a[i-1]*(k-1) + b[i-1] * (k-2)
    return a[n-1]