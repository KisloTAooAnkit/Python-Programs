def minMax(arr):
    mn,mx = 0,0
    
    n = len(arr)
    
        # If array has even number of elements then
    # initialize the first two elements as minimum
    # and maximum
    if n%2==0:
        mn = min(arr[0],arr[1])
        mx = max(arr[0],arr[1])
        i=2    
        
        # If array has odd number of elements then
    # initialize the first element as minimum
    # and maximum
    else:
        mn,mx = arr[0],arr[0]
        i=1
    
    # In the while loop, pick elements in pair and
    # compare the pair with max and min so far
    
    while(i<n-1):
        if(arr[i]<arr[i+1]):
            mn = min(arr[i],mn)
            mx = max(arr[i+1],mx)
        else:
            mn = min(arr[i+1],mn)
            mx = max(arr[i],mx)
        i+=2
    
    return mn,mx

arr = [4,3,2,1,0,7]
print(minMax(arr))
            