from copy import deepcopy
def dfs(grid,i,j,m,n,zeroCount,ans):
    if i >= m or i < 0 or j >= n or j < 0:
        return  
    if grid[i][j] == -1:
        return 
    if grid[i][j] == 2:
        if zeroCount == 0:
            ans[0] +=1
        return
    grid[i][j] = -1
    b = deepcopy(grid)
    dfs(b,i,j+1,m,n,zeroCount-1,ans)
    dfs(b,i-1,j,m,n,zeroCount-1,ans)
    dfs(b,i+1,j,m,n,zeroCount-1,ans)
    dfs(b,i,j-1,m,n,zeroCount-1,ans)
    grid[i][j] = 0
    return





def uniquPathsIII(grid):
    rows = len(grid)
    cols = len(grid[0])
    zeroCount = 1
    ans = [0]
    x,y = 0,0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                zeroCount +=1
            if grid[i][j] == 1:
                x,y = i,j
    
    dfs(grid,x,y,rows,cols,zeroCount,ans)
    return ans


grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
print(uniquPathsIII(grid))