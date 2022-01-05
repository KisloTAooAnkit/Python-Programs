######################### Recursive DP ################################
def helper(n,dp):
    
    if n==1:
        return 0
    
    if n == 2:
        return 1
    
    if n in dp:
        return dp[n]
    
    ans = (n-1)*(helper(n-1,dp) + helper(n-2,dp))
    dp[n] = ans
    return ans
def countDearrangementRecursive(n):
    dp = dict()
    return helper(n,dp)

n = 4
print(countDearrangementRecursive(4))
##################################################################################

############################### ITerative #######################################
def solIterative(n):
    dp = [0]*(n+1)
    dp[1] = 0
    dp[2] = 1
    
    for i in range(3,n+1):
        dp[i] = (i-1)*(dp[i-1]+dp[i-2])
    return dp[n]
############################################################################