import math
def isPossible(eatingPow,piles,h,n):
    count = h
    i = 0
    while(i<n):
        if(piles[i]%eatingPow==0):
            count -= piles[i]//eatingPow
        else:
            count -= math.ceil(piles[i]/eatingPow)
        i+=1
        if(count<0):
            return False
    
    return True
            

def minEatingSpeed(piles, h):
    n = len(piles)
    if(n==h):
        return max(piles)
    ans = 0
    end = sum(piles)
    start = 1
    while(start<=end):
        mid = start + (end-start)//2

        if(isPossible(mid,piles[:],h,n)):
            ans = mid
            end = mid-1
        else:
            start = mid+1
    return ans
    
a = [30,11,23,4,20]
h = 6
print(minEatingSpeed(a,h))