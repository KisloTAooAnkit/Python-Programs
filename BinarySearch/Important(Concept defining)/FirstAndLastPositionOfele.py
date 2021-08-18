#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
def searchRange(arr,target):
    start = 0
    n = len(arr)
    end = n-1
    firstOccr = -1
    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid] == target):
            firstOccr = mid
            end = mid-1
            if(end <0):
                break
        elif(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
    
    start = 0
    end = n-1
    secondOccr = -1
    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid] == target):
            secondOccr = mid
            start = mid+1
            if(start>=n):
                break
        elif(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
        
     
    return [firstOccr,secondOccr]
    
    
arr = [5,7,7,7,8,8,10]
n = 0
print(searchRange(arr,n))