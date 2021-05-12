import sys
#https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution:
    def increasingTriplet(self, arr) -> bool:
        n= len(arr)
        if(n<=0):
            return False
        n1lowestcand = arr[0]
        n2lowestcand = sys.maxsize
        maxsize = 1

        for i in range(1,n):
            currelement = arr[i]
            if(n1lowestcand>=currelement):
                n1lowestcand = currelement
            else:
                if(n2lowestcand<currelement):
                    maxsize = 3
                else:
                    n2lowestcand = currelement
                    maxsize = 2
            if(maxsize == 3):
                return True

        return False
        