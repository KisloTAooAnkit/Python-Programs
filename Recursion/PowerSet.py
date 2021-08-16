
def helper(arr,n,ans,temp):
    if(n==0):
        ans.append(temp)
        return 
    
    temp.append(arr[0])
    print(temp)
    helper(arr[1:],n-1,ans,temp[:])
    temp.pop(-1)
    helper(arr[1:],n-1,ans,temp[:])
    return 


def subsets(nums):
    ans = []
    helper(nums,len(nums),ans,[])
    print(ans)


arr = []
subsets(arr)