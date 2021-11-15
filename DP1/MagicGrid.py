from typing import AnyStr


def MagicGrid(grid):
    row = len(grid)
    col = len(grid[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]

    dp[row-1][col-1] = 1 if grid[row-1][col-1] > 0 else -grid[row-1][col-1] +1
    
    prev = dp[row-1][col-1]
    for j in range(col-2,-1,-1):
        val = prev - grid[row-1][j]
        dp[row-1][j] = 1 if val <= 0 else val
        prev = dp[row-1][j]
    
    prev = dp[row-1][col-1]
    for i in range(row-2,-1,-1):
        val = prev - grid[i][col-1]
        dp[i][col-1] = 1 if val <= 0 else val
        prev = dp[i][col-1]
    
    for i in range(row-2,-1,-1):
        for j in range(col-2,-1,-1):
            val = min(dp[i+1][j],dp[i][j+1]) - grid[i][j]
            val = 1 if val <= 0 else val
            dp[i][j] = val
    return dp[0][0]
            
    
def magicGridRecur(grid,si,sj,ei,ej):
    if si == ei  and sj == ej:
        return 1 if grid[si][sj] > 0 else -grid[si][sj] +1
    if si >ei or sj>ej:
        return float("inf")
    
    ans1 = magicGridRecur(grid,si+1,sj,ei,ej)
    ans2 = magicGridRecur(grid,si,sj+1,ei,ej)
    
    val = min(ans1,ans2)
    val = val - grid[si][sj]
    if val <= 0:
        return 1 
    return val
    
    
    
grid = [
    [-2,-3,3],
    [-5,-10,1],
    [10,30,-5]
        ]
print(MagicGrid(grid))