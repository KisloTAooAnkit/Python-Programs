
"""
naive recursive
"""
def canJumpSol(arr,si,n):
    if(si >= n-1):
        return True
    if(arr[si]==0):
        return False

    maxsteps = si + arr[si]

    ans = False

    for i in range(maxsteps,si,-1):
        ans  = ans or canJumpSol(arr,i,n)
    
    return ans 

'''
recursive + memoization O(n^2) TC , O(n) space complexity 
'''
def canJumpSol_Dp(arr,si,n,dp):
    if(si >= n-1):
        return True
    if(arr[si]==0):
        return False

    if(dp[si] != -1):
        return dp[si]

    maxsteps = si + arr[si]

    ans = False

    for i in range(maxsteps,si,-1):
        ans  = ans or canJumpSol_Dp(arr,i,n,dp)

    
    dp[si] = ans
    return ans 

'''
Iterative DP TC O(n^2) , SC O(n)
'''
def canJumpSol_I(arr):
    n = len(arr)
    dp=[False for i in range(n)]
    dp[-1] = True

    for i in range (n-2,-1,-1):
        val = i + arr[i] if i + arr[i] < n else n 
        for j in range(i+1,val+1):
            if(dp[j]):
                dp[i] = True
                break
    return dp[0]


'''
Effiecent Iterative DP or "greedy" TC : O(n) , SC O(1)
'''        
def canJumpSol_I_optimized(arr):
    n = len(arr)
    last_good_index = n-1
    for i in range (n-2,-1,-1):
        val = i + arr[i] if i + arr[i] < n else n 
        if val >= last_good_index:
            last_good_index = i 
    
    return last_good_index == 0 


nums = [3,2,1,0,4]


#https://leetcode.com/problems/jump-game/
def canJump(nums):
    dp = [-1 for i in range(len(nums))]
    
    return canJumpSol_I_optimized(nums)

print(canJump(nums))