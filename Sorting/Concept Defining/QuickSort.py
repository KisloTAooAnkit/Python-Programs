def quickSort(arr,start,end):
    if(start<end):
        part = Partition(arr,start,end)
        quickSort(arr,start,part-1)
        quickSort(arr,part+1,end)
    
def Partition(arr,low,high):
    pivot_idx = low
    pivot = arr[pivot_idx]

    while(low<high):

        while(low < len(arr) and arr[low]<=pivot):
            low+=1

        while(arr[high]>pivot):
            high-=1
        
        if(low<high):
            arr[low],arr[high] = arr[high],arr[low]

    arr[pivot_idx],arr[high] = arr[high],arr[pivot_idx]

    return high


arr = [9,8,2,6,100,4,13,42,1]
quickSort(arr,0,len(arr)-1)
print(arr)        

