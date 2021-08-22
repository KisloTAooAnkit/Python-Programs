def quickSort(difficulty,profit,start,end):
    if(start<end):
        part = Partition(difficulty,profit,start,end)
        quickSort(difficulty,profit,start,part-1)
        quickSort(difficulty,profit,part+1,end)
    
def Partition(difficulty,profit,low,high):
    pivot_idx = low
    pivot = difficulty[pivot_idx]

    while(low<high):

        while(low < len(difficulty) and difficulty[low]<=pivot):
            low+=1

        while(difficulty[high]>pivot):
            high-=1
        
        if(low<high):
            difficulty[low],difficulty[high] = difficulty[high],difficulty[low]
            profit[low],profit[high] = profit[high],profit[low]

    difficulty[pivot_idx],difficulty[high] = difficulty[high],difficulty[pivot_idx]
    profit[pivot_idx],profit[high] = profit[high],profit[pivot_idx]

    return high




def floorsearch(arr,target,start,end):
    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid] == target):
            return mid
        if(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return end




def maxProfitAssignment(difficutly,profit,worker):
    n = len(difficutly)
    m = len(worker)
    quickSort(difficutly,profit,0,n-1)
    for i in range(1,n):
        if(profit[i-1]>profit[i]):
            profit[i] = profit[i-1]
    ans = 0
    for i in range(0,m):
        idx = floorsearch(difficutly,worker[i],0,n-1)
        
        if(idx>=0):
            
            ans +=profit[idx]
    
    return ans
    


worker = [92,10,85,84,82]
diff = [68,35,52,47,86]
profit = [67,17,1,81,3]
print(maxProfitAssignment(diff,profit,worker))