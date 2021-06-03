#https://leetcode.com/problems/jump-game-ii/

#piche se dp lagaya
def jumpDP(nums):
    n = len(nums)
    dp = [0 for i in range(n)]
    for si in range(n-2,-1,-1):
        val = nums[si]
        if(val+si>= n-1 ):
            dp[si] = 1
        else:
            start = si+1
            end = si + val + 1
            dp[si] = 1+min(dp[start:end])
    
    print(dp)
    print(nums)
    print(dp[0])

#wasnt able to understand this logic 
def jumpsOptimizedGreedy(nums):
    n=len(nums)
    jumpcount = 0
    left = 0
    right = 0
    i=0
    while i < n-1:
        left = i+1
        right = nums[i]+i if nums[i] + i <n-1 else n-1
        maximum=0
        maxindex =0
        for j in range(left,right+1):
            if(nums[j]>=maximum):
                maximum = nums[j]
                maxindex = j

        i = maxindex
        jumpcount+=1
    return jumpcount


#my submission (leetcode)
def jumpGame_2(arr):
    n= len(arr)

    if(n<=1):
        return 0

    start = 0
    end = 0
    i =0 
    totalJumps = 0


    while(i<n-1):
        start = i+1
        end = arr[i] + i if arr[i] + i < n-1 else n-1
        farthest_index = 0
        farthest_index_val = 0
        for j in range(start,end+1):
            val = j + arr[j] 
            val = val if val<n-1 else n-1
            if(val>=farthest_index_val):
                farthest_index_val = val
                farthest_index = j
                
        
        i = farthest_index
        totalJumps +=1
    
    return totalJumps


nums1 = [2,3,1,4,8]
print(jumpGame_2(nums1))




