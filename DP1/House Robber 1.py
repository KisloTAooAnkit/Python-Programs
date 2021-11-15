def helper(n,nums):
    if n==0:
        return nums[0]
    if n==1:
        return max(nums[0],nums[1])
    
    option1 = nums[n] + helper(n-2,nums)
    option2 = helper(n-1,nums)
    ans = max(option1,option2)
    return ans

def houseRobberDp(n,nums,dp):
    if n== 0:
        return nums[0]
    if n==1:
        return max(nums[0],nums[1])
    if dp[n]>-1:
        return dp[n]
    ans1 = nums[n] + houseRobberDp(n-2,nums,dp) 
    ans2 =  houseRobberDp(n-1,nums,dp) 
    dp[n] = max(ans1,ans2)
    return dp[n]
    
def houseRobberIterative(nums):
    n = len(nums)
    if n <=2:
        return max(nums)
    dp = [0]*(n+1)
    dp[0] =  nums[0]
    dp[1] = max(nums[0],nums[1])

    for i in range(2,n):
        a = dp[i-2] + nums[i]
        b = dp[i-1]
        dp[i] = max(a,b)
    print(dp)
    return dp[n-1]
        

def houseRobber(nums):
    n = len(nums)
    dp = [-1] * (n+1)
    ans1 = helper(n-1,nums)
    ans2 = houseRobberDp(n-1,nums,dp)
    ans3 = houseRobberIterative(nums)
    return ans1,ans2,ans3
arr = [2,1,1,2]
print(houseRobber(arr))