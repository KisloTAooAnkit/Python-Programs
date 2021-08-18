def searchNearlySorted(arr,target):
    start = 0
    n = len(arr)
    end = n-1

    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid] == target):
            return mid
        if(mid-1 >start and arr[mid-1] == target):
            return mid-1
        
        if(mid+1<end and arr[mid+1] == target):
            return mid+1
        
        if(arr[mid]<target):
            start = mid+2
        
        else:
            end = mid-2
    
    return -1