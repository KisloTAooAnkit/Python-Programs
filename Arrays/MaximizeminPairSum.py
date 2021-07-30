import sys
def minPairSum(arr):
    arr.sort()
    low = 0
    high = len(arr)-1
    maxpair = -sys.maxsize 
    while(low<high):
        maxpair = max(arr[low]+arr[high],maxpair)
        low+=1
        high-=1
    
    return maxpair


ar = [3,5,4,2,4,6]

print(minPairSum(ar))
        
    