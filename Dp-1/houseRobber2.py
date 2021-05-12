# def rob(arr,n,flag):
#     if(n<0):
#         return 0
    
#     if(n==0 and flag):
#         return 0 
    
    
#     res1 = rob(arr,n-1,False)
#     res2 = arr[n] + rob(arr,n-2,True)
#     return max(res1,res2)

#https://leetcode.com/problems/house-robber-ii/

def robAdv(nums):
    n= len(nums)
    output=[0]*n
    
    if(n<=2):
        return max(nums)
    
    output[0] = nums[0]
    output[1] = max(nums[0],nums[1])
    for i in range(2,n):
        output[i] = max(output[i-1],output[i-2] + nums[i])
    
    print(output)
    return max(output)
    

        
def caller(arr,n):
    #second ele to last
    ans1 = robAdv(arr[1:])
    #first ele to secondlast
    ans2 = robAdv(arr[:-1])

    return(max(ans1,ans2))

    
a=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


print(caller(a,len(a)))

