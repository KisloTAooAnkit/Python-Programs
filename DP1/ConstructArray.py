def countSubarrays(n,k,x):
    if n==1 and x != 1:
        return (0,1)
    if n==1 and x ==1:
        return (1,0)

    mod = (10**9) + 7    
    prevnumberofXs,prevNonXs = countSubarrays(n-1,k,x)
    this2s = prevNonXs
    thisNon2s = (k-1)*prevnumberofXs + prevNonXs*(k-2)
    return (this2s%mod,thisNon2s%mod) 


def constructArray(n,k,x):
    a = [0]*n
    b = [0]*n
    mod = (10**9) + 7
    a[0] = 1 if x == 1 else 0
    b[0] = 0 if x == 1 else 1
    for i in range(1,n):
        nonXs = (k-1)*a[i-1] + (k-2)*b[i-1]
        Xs = b[i-1]
        a[i] = Xs%mod
        b[i] = nonXs%mod
    return a[n-1]

n = 4
k = 3
x = 2
print(countSubarrays(n,k,x)[0])

