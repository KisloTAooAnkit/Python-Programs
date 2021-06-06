def nonOverLappingIntervals(arr):
    n=len(arr)
    if(n<=1):
        return 0
    arr.sort()
    last_interval = arr[0]
    count =0 

    for i in range(1,n):

        nxt_interval = arr[i]

        if(not checkForMerge(last_interval,nxt_interval)):
            last_interval = nxt_interval
            
        else:
            last_interval = last_interval if last_interval[1]< nxt_interval[1] else nxt_interval
            count+=1
    
    return count
        

    
def checkForMerge(prev_interval,curr_interval):
    return prev_interval[1]>curr_interval[0]


arr = [[1,2],[2,3]]

print(nonOverLappingIntervals(arr))
        
    
