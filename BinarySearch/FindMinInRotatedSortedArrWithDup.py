def findMin(arr):
    n = len(arr)
    start = 0
    end = n-1

    if n== 1:
        return arr[0]
    
    while(start<=end):
        mid = start + (end-start)//2

        if arr[mid] > arr[start]:
            mid = start +1
        
        elif arr[mid] < arr[end]:
            end = mid
        else:
            end -=1

    return arr[end]