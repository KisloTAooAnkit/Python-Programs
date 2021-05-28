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


    
        








nums = [2,3,0,1,4]
print(jumpsOptimizedGreedy(nums))




