def singleNum(arr):
    resXor = 0
    for i in arr:
        resXor ^= i
    lsb = resXor & -resXor
    ans = [0,0]
    for i in arr:
        if lsb & i == 0:
            ans[0] ^= i
        else:
            ans[1] ^= i
    return ans
    