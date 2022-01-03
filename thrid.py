def maxProductSubarray(arr):
    n = len(arr)
    pos = [0]*n
    neg = [0]*n
    pl = [1]*n
    nl = [1]*n

    pos[0],neg[0] = arr[0],arr[0]
    for i in range(1,n):
        val = arr[i]
        if val < 0:
            pp = neg[i-1]*val 
            np = pos[i-1]*val
            pp = max(neg[i-1]*val,val)
            np = min(pos[i-1]*val,val)
            pos[i] = pp
            neg[i] = np
        if val >0:
            pp = max(pos[i-1]*val,val)
            np = min(neg[i-1]*val,val)
            pos[i] = pp
            neg[i] = np
        if val == 0:
            pos[i] = 0
            neg[i] = 0
    return max(max(pos),max(neg))

arr = [-2,0,-1]

print(maxProductSubarray(arr))