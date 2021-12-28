from collections import defaultdict
def dfs(n,i,j,dp,tri,cols):

    if j >= cols:
        return float("inf")
    if n ==0:
        return 0
    
    ans1 = tri[i][j] + dfs(n-1,i+1,j,dp,tri,cols+1)
    ans2 = tri[i][j] + dfs(n-1,i+1,j+1,dp,tri,cols+1)

    return min(ans1,ans2)



def minTotal(tri):
    dp = defaultdict(lambda : -1)
    n = len(tri)
    cols = 1
    return dfs(n,0,0,dp,tri,cols)


def solve(tri):

    n = len(tri)
    dp = tri[n-1][:]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[j] = min(dp[j],dp[j+1]) + tri[i][j]
    return dp[0]
     

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(solve(triangle))
