
import re


def helper(questions,i,n,dp):
    if i >= n:
        return 0
    if dp[i] != -1:
        return dp[i]
    
    pick = helper(questions,i+questions[i][1]+1,n,dp) + questions[i][0]
    skip = helper(questions,i+1,n,dp)
    dp[i] = max(pick,skip)
    return dp[i]



def solve(questions):
    n = len(questions)
    dp = [-1 for _ in range(n+1)]
    return helper(questions,0,n,dp)

q =[[1,1],[2,2],[3,3],[4,4],[5,5]]
print(solve(q))














# def helper(questions,i,n,cooldown,cd,dp):
#     if n == 0:
#         return 0
#     if dp[n][cd] != -1:
#         return dp[n][cooldown]
    
#     if cooldown>0:
#         return helper(questions,i+1,n-1,cooldown-1,cd,dp)
    
#     pick = questions[i][0] + helper(questions,i+1,n-1,questions[i][1],1,dp)
#     skip = helper(questions,i+1,n-1,cooldown,0,dp)
#     dp[n][cooldown] = max(pick,skip)
#     return max(pick,skip)