
#https://leetcode.com/problems/house-robber/

def farida(nums,n):
    output=[0]*n
    
    if(n<=2):
        return max(nums)
    
    output[0] = nums[0]
    output[1] = max(nums[0],nums[1])
    for i in range(2,n):
        output[i] = max(output[i-1],output[i-2] + nums[i])
        
    print(output)
    return max(output)
 
 
#no extra array   
def faridaOPt(nums,n):
    prevsum,currsum=0,0
    
    if(n<=2):
        return max(nums)
    
    prevsum = nums[0]
    currsum = max(nums[0],nums[1])
    for i in range(2,n):
        ans = max(currsum,prevsum + nums[i])
        prevsum = currsum
        currsum = ans
        
    return currsum

    
    
a=[100,70,30,20,10]

farida(a,len(a))
         