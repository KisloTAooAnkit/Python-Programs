def answer(arr,k):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    revPrefix = [arr[n-1]]*n

    for i in range(1,n):
        prefix[i] = prefix[i-1] + arr[i]
    for i in range(n-2,-1,-1):
        revPrefix[i] = revPrefix[i+1] + arr[i]
    

    

