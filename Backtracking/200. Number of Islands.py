def dfs(grid,i,j,m,n):
    if i >= m or i < 0 or j >= n or j < 0:
        return 
    if grid[i][j] == "0":
        return 
    grid[i][j] = "0"
    dfs(grid,i+1,j,m,n)
    dfs(grid,i-1,j,m,n)
    dfs(grid,i,j+1,m,n)
    dfs(grid,i,j-1,m,n)
    
    return

def numOfIsland(grid):
    ans = 0
    
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                dfs(grid,i,j,rows,cols)
                ans +=1
    return ans

grid =[
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]

print(numOfIsland(grid))