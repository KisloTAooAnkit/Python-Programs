def productArray(arr):
    n = len(arr)
    ans = [1]*n
    prevProduct = 1
    for i in range(0,n):
        ans[i] = ans[i]*prevProduct
        prevProduct = arr[i]*prevProduct
    
    prevProduct =1
    for i in range(n-1,-1,-1):
        ans[i] = ans[i]*prevProduct
        prevProduct = arr[i]*prevProduct
    return ans