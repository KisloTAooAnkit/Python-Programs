import re


def maxProductSubset(arr, n):
    negC,posC,zeroC = 0,0,0
    pp, np = 1,1
    minNeg = float("-inf")
    mod = 10**9 + 7
    for i in arr:
        if i<0:
            minNeg = max(minNeg,i)
            np*=i
            negC +=1
        if i>0:
            posC +=1
            pp*=i
        else:
            zeroC +=1
    if negC == 0:
        if posC>0:
            return pp%mod
        else:
            return 0
    if negC>0:    
        if negC %2 != 0:
            np = np//abs(minNeg)
        if np < 0:
            if posC>0:
                return pp%mod
            else:
                if zeroC > 0:
                    return 0
                else:
                    return np%mod
        return (np*pp)%mod
        
    

arr = [2,-1,-1,-3,-3,-5,-6]
print(maxProductSubset(arr,len(arr)))