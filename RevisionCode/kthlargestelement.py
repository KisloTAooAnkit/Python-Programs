def partition(arr,low,high):

    pivot = arr[low]
    pivot_idx = low

    i = low
    j = high

    while(low<high):
            
        while(low<len(arr) and arr[low]<=pivot):
            low+=1

        while(arr[high]>pivot):
            high-=1

        if(low<high):
            arr[high],arr[low] = arr[low],arr[high]
    
    arr[pivot_idx],arr[high] = arr[high],arr[pivot_idx]

    return high


def kthLargestAns(arr,k,low,high):



    if(len(arr) <1):
        return -1

    if(low<=high):
            
        n= len(arr)
        partition_idx = partition(arr,low,high)
        ans_idx = n-k
        
        if(partition_idx == ans_idx):
            return arr[partition_idx]
        
        elif(partition_idx > ans_idx):
            high = partition_idx-1
        
        elif(partition_idx<ans_idx):
            low = partition_idx +1
        
        return kthLargestAns(arr,k,low,high)


arr = [3,2,3,1,2,4,5,5,6]

k = 0

print(kthLargestAns(arr,k,0,len(arr)-1))