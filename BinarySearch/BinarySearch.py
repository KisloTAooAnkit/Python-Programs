def binarysearch(arr,n):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid =  (start + end)//2   #start + (end - start)//2 #avoiding integer overflow in otherlanguages
        if arr[mid] == n:
            return mid
        elif(arr[mid]>n):
            end = mid-1
        else:
            start = mid+1
    
    return -1


a = [1,2,3,4,4,5,6,8,52,110,333,232332]
print(binarysearch(a,52))

