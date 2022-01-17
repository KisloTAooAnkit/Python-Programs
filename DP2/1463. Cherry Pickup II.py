

def dfs(row,col1,col2,grid,dp):
    
    if row == len(grid) or col1 < 0 or col1 >= len(grid[0]) or col2 < 0 or col2 >= len(grid[0]):
        return 0
    
    
    ans = grid[row][col1]
    
    if dp[row][col1][col2] != -1:
        return dp[row][col1][col2]
    
    if col1 != col2:
        ans +=grid[row][col2]
     
    res = 0
    for i in [col1,col1-1,col1+1]:
        for j in [col2,col2+1,col2-1]:
            res = max(res,dfs(row+1,i,j,dp))
    dp[row][col1][col2] = res + ans
    return dp[row][col1][col2]



def cherrypickup(grid):
    row = len(grid)
    col = len(grid[0])
    dp = [[[-1]*col for _ in range(col+1)] for _ in range(row+1)]
    return dfs(0,0,col-1,grid,dp)