def canPartitionKSubsets(arr,k):
    val = sum(arr)
    if val%k != 0:
        return False
    ans = val//k 
    dic = dict()
    for val in arr:
        if val in dic:
            dic[val] +=1
        else:
            dic[val] = 1
    arr.sort()
    
    for key in arr:
        if key > ans:
            return False
        
        if dic[key] == 0:
            continue
        newKey = ans-key
        if newKey == 0:
            dic[key] -=1
            
        elif newKey in dic:
            dic[newKey] -=1
            dic[key] -=1
            
            
            
    for key in dic:
        if dic[key] > 0:
            return False
    
    
    return True