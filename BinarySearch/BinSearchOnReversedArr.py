def binreverse(arr,n):
    start = 0
    end = len(arr) -1
    while(start<=end):
        mid = start + (end-start) //2
        if arr[mid] == n:
            return mid
        elif arr[mid]>n:
            start = mid+1
        else:
            end = mid-1
    
    return -1            

num = 7

arr=[10,9,8,7,6,5,4,3,2,1]

print(binreverse(arr,num))