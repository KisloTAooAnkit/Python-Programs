
def dfs(grid,i,j,m,n):
    if i >= m or i < 0 or j >= n or j < 0:
        return 0
    if grid[i][j] == 0:
        return 0
    grid[i][j] = 0
    ans1 = dfs(grid,i+1,j,m,n)
    ans2 = dfs(grid,i-1,j,m,n)
    ans3 = dfs(grid,i,j+1,m,n)
    ans4 = dfs(grid,i,j-1,m,n)
    
    return 1 + ans1 + ans2 + ans3 + ans4

def maxArea(grid):
    globalMax = 0
    
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                globalMax = max(globalMax,dfs(grid,i,j,rows,cols))
    return globalMax
                
    