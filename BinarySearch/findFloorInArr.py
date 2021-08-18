def findFloor(arr,target):
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
    
    if(end == -1):
        return -1
    else:
        return arr[end]

arr = [1]
print(findFloor(arr,3))




