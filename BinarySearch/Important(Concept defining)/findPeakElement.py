#Important
"""binary search on unsorted array (where we define our own criterial for divide and conq)"""
import sys
def findPeakElement(arr):
    start = 0
    n = len(arr)
    end = n-1
    while(start<=end):
        mid = start + (end-start)//2
        #check for peak
        prev = -sys.maxsize if mid-1 < 0 else arr[mid-1]
        nxt = -sys.maxsize if mid+1 >= n else arr[mid+1]
        if(arr[mid]>prev and arr[mid]>nxt):
            return mid
        #find next half where ans is probable
        if(arr[mid]<prev):
            end = mid-1
        elif(arr[mid]<nxt):
            start = mid+1

arr = [1]

print(findPeakElement(arr))