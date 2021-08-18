def findEle(arr):
    start = 0
    n = len(arr)
    end = n-1
    if(n<=2):
        return -1
    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid]>arr[mid-1] and arr[mid+1]<arr[mid]):
            return arr[mid] 
        elif(arr[mid]<arr[mid-1]):
            end = mid-1
        elif(arr[mid]<arr[mid+1]):
            start = mid+1
    
arr = [1,4,8,3,2]
print(findEle(arr))