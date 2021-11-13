#https://leetcode.com/problems/subarray-product-less-than-k/
def numSubarrayProductLessThanK(nums,k):
    if(k<=1):
        return 0
        
    n = len(nums)
    start = 0
    end = 0
    rp = 1
    ans = 0
    
    #2 while-loops are deciding sliding window size
    #for a particular size we do ans+=end-start +1 
    
    while(end<n):
        rp = rp*nums[end]
        while(rp>=k):
            rp = rp//nums[start]
            start+=1
        
        ans += end - start + 1 # yeh formula kaisa aaya uska explanation https://www.youtube.com/watch?v=SxtxCSfSGlo ke comments mein 
        # shubham goel ka comment dekhna.
        end+=1
        
    return ans


arr = [10,5,2,6]
k = 100

print(numSubarrayProductLessThanK(arr,k))