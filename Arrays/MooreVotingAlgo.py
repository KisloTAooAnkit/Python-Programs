def majorityElement(arr,n):
    res = arr[0]
    count = 1
    for i in range(1,n):
        if(res == arr[i]):
            count+=1
        elif(res!=arr[i]):
            count-=1
            if(count==0):
                count = 1
                res = arr[i]
    count =0
    for i in range(n):
        if(arr[i]==res):
            count+=1
    
    if(count>n/2):
        return res
    else:
        return -1
        
