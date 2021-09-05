def countPairs(arr,start,end,target,firstele,secondele):
    count = []
    while(start<end):
        if(arr[start]+arr[end]==target):
            count.append([secondele,arr[start],arr[end]])
            start+=1
        elif(arr[start]+arr[end]<target):
            start+=1
        else:
            end-=1
    return count

def threeSum(arr,n,start,target,firstele):
    ans = []
    for i in range(start,n-2):
        fixd = arr[i]
        pairTarget = target-fixd
        ans.append(countPairs(arr,i+1,n-1,pairTarget,firstele,fixd))
    return ans

def fourSum(arr,k):
    arr.sort()
    n = len(arr)
    ans = []
    for i in range(n-3):
        fixd = arr[i]
        tripTarget = k - fixd
        res = threeSum(arr,n,i,fixd)
        ans.append(res) 
    return ans
