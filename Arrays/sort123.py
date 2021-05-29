def sort012(arr):
    low = 0
    high = len(arr)-1
    mid = 0
    
    while(mid<len(arr)):
        val = arr[mid]
        if(val==1):
            mid+=1
        elif(val==0):
            arr[mid],arr[low] = arr[low],arr[mid]
            low+=1
            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
            mid+=1
    
    return arr

arr = [2,1,2,1,0,0,2,1,0]

print(sort012(arr))
        