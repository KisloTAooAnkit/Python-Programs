def solve(arr,k):
    arr.sort()
    
    n = len(arr)
    i=0
    while(k and i<n):
        if arr[i]<0:
            arr[i] = -arr[i]
            i+=1
            k-=1
        else:
            if k%2 != 0:
                arr[i] = -arr[i]
            k=0
    return sum(arr)
                
    