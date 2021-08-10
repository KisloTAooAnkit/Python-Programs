

def helperQuickPartition(arr,number,low,high):

    pivot = number
    n = len(arr)

    while(low<high):
        
        while(low<n and arr[low]<=pivot):
            low+=1

        while(arr[high]>pivot):
            high -=1
        
        if(low<high):
            arr[low],arr[high] = arr[high],arr[low]
        
    
    return high





def threeWayPartition(arr,a,b):
    n = len(arr)

    if(n<2):
        return 0
    partIdx = 0
    if(a>b):
        a,b = b,a

    partIdx = helperQuickPartition(arr,a,0,n-1)
    print(arr,partIdx)
    partIdx = helperQuickPartition(arr,b,partIdx+1,n-1)
    print(arr,partIdx)
    return 1 

arr = [6 ,22 ,68, 5, 14, 62, 55 ,27, 60, 45, 3 ,3 ,7, 85]
a = 22
b = 64

print(threeWayPartition(arr,a,b))
