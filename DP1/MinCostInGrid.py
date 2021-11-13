def MinCostInGridRecursive(grid,ci,cj,ei,ej):
    if ci == ei and cj == ej:
        return grid[ci][cj]
    
    if ci > ei or cj > ej:
        return float("inf")
    
    path1 = MinCostInGridRecursive(grid,ci+1,cj,ei,ej)
    path2 = MinCostInGridRecursive(grid,ci,cj+1,ei,ej)
    return grid[ci][cj] +  min(path1,path2)

def DP_Recursive(grid,dp,ci,cj,ei,ej):
    if ci == ei and cj == ej:
        return grid[ci][cj]
    
    if ci > ei or cj > ej:
        return float("inf")
    
    if dp[ci][cj] != -1:
        return dp[ci][cj]
    
    path1 = DP_Recursive(grid,ci+1,cj,ei,ej)
    path2 = DP_Recursive(grid,ci,cj+1,ei,ej)
    dp[ci][cj] = grid[ci][cj] +  min(path1,path2)
    return dp[ci][cj]

def DP_Iterative(grid):
    row = len(grid)
    col = len(grid[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[row-1][col-1] = grid[row-1][col-1]
    
    #rowBase case
    prev = 0
    for i in range(row-1,-1,-1):
        dp[i][col-1] = prev + grid[i][col-1]
        prev = dp[i][col-1]
    
    #col basecase
    prev = 0
    for j in range(col-1,-1,-1):
        dp[row-1][j] = prev + grid[row-1][j]
        prev = dp[row-1][j]
    
    #fill rest Of cells
    for i in range(row-2,-1,-1):
        for j in range(col-2,-1,-1):
            dp[i][j] = grid[i][j] +  min(dp[i+1][j],dp[i][j+1])
    return dp[0][0]

def minPathSum(grid) -> int:

    return DP_Iterative(grid)


grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
    ]
print(minPathSum(grid))