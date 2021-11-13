

#https://leetcode.com/problems/unique-paths-ii/

def UniquePathObs(grid,currx,curry,endx,endy,dp):
    if(currx==endx and curry==endy):    
        return 1
    
    
    if(currx>endx or curry>endy ):
        return 0
    
    if(grid[currx][curry] == 1):
        return 0

    
    if(dp[currx][curry] != -1):
        return dp[currx][curry]
    
    ans=0
    ans += UniquePathObs(grid,currx+1,curry,endx,endy,dp)
    ans += UniquePathObs(grid,currx,curry+1,endx,endy,dp)
    
    dp[currx][curry] = ans
    
    return ans


def caller(grid):
    m = len(grid)
    n = len(grid[0])
    
    if(grid[m-1][n-1] == 1):
        return 0
    
    dp = [ [-1 for j in range(n)] for i in range(m) ]

    return UniquePathObs(grid,0,0,m-1,n-1,dp)



arr = [[0,0,0],[0,1,0],[0,0,0]]
print(caller(arr))