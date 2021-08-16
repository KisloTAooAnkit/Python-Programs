def countNumberOfOcc(arr,target):
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
        
     
    return secondOccr - firstOccr +1

arr = [1, 1, 2, 2, 2, 2, 3]
target = 2

print(countNumberOfOcc(arr,2))
    