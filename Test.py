def sol(arr):

    zeroC = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            zeroC+=1
    ans = float("inf")
    onesC = 0
    for i in range(n):
        if arr[i] == 0:
            zeroC-=1

            ans = min(ans,zeroC+onesC)
        
        if arr[i] == 1:
            ans = min(ans,zeroC+onesC)
            onesC+=1
    return ans
    