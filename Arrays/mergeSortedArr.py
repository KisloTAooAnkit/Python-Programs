

def customBsearch(arr,val,n):
    low = 0
    high = n-1
    
    while(low<high):
        mid = (low+high)//2
        
            
        
        if(val>arr[mid]):
            low = mid+1
        elif(val<arr[mid]):
            high = mid-1
        
        if(low == high):
            break
        elif(val == arr[mid]):
            return mid
            
        
        
    
    return low