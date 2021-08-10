
def helper(arr,n,ans):
    if(n==0):
        ans.append([])
        return ans
    
    ans.append(arr[0])
    helper(arr[1:],n-1,ans)
    ans.pop(-1)
    helper(arr[1:],n-1,ans)
    
    return ans

def subsets(nums):
    ans = []
    return helper(nums,len(nums),ans)


arr = [1,2,3]
print(subsets(arr))