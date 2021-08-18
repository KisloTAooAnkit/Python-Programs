def findCeil(arr,target):
    start = 0
    n = len(arr)
    end = n-1
    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid] == target):
            return arr[mid]
        
        if(arr[mid]<target):
            start = mid+1
        
        else:
            end = mid-1
    
    return start

arr1 = [1]
arr = [1,3,5,6]
print(findCeil(arr,2))