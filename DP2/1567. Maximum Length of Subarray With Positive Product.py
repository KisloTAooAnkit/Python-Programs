def getMaxLen(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] ==0:
            continue
        arr[i]//=arr[i]
    posL = 1
    negL = 1
    pos,neg = arr[0],arr[0]

    maxL = 0
    for i in range(1,n):

        val = arr[i]
        currPos,currNeg = 0,0
        cpl,cnl = 1,1
        if val < 0:
            #pp
            if val*neg >= val:
                currPos = val*neg
                cpl = negL+1
            else:
                currPos = val

            #np
            if val*pos <= val:
                currNeg = val*pos
                cnl = posL+1
            else:
                currNeg = val 
            
        if val >0:
            if val*pos >= val:
                currPos = val*pos
                cpl = posL +1
            else:
                currPos = val

            if val*neg <= val:
                currNeg = val*neg
                cnl = negL+1
            else:
                currNeg = val
        
        if val == 0:
            currPos = 0
            currNeg = 0
        pos = currPos
        neg = currNeg
        posL = cpl
        negL = cnl
        if currPos > 0:
            maxL = max(maxL,cpl)
        if currNeg >0:
            maxL = max(maxL,cnl)

    return maxL


arr =[-1,-2,-3,0,1]
print(getMaxLen(arr))