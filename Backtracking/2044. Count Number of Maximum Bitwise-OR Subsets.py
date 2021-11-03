
def calcOR(arr):
    ans = 0
    for i in arr:
        ans = ans | i
    return ans

def DfsHelper(arr,ans,value,idx,n):
    if idx >= n:
        currVal = calcOR(arr)
    
        if currVal > value[0]:
   
            ans[0] = 1
            value[0] = currVal
    
            
            
        elif currVal == value[0]:
            ans[0] +=1
           
        return

    cache = arr[idx]
    arr[idx] = 0
    DfsHelper(arr,ans,value,idx+1,n)
    arr[idx] = cache
    DfsHelper(arr,ans,value,idx+1,n)
    return
    
def countMaxSubsets(arr):
    ans = [0]
    val = [float("-inf")]
    n = len(arr)
    DfsHelper(arr,ans,val,0,n)
    return ans[0]
    
    
arr = [3,1]
print(countMaxSubsets(arr))
