def largestMatrix(grid):
    rows = len(grid)
    cols = len(grid[0])
    one = "1"
    zero = "0"
    dp = [[0]*cols for _ in range(rows)]

    ans = 0
    for i in range(cols):
        if grid[0][i] == one:
            dp[0][i] = 1
            ans = 1
    
    for i in range(rows):
        if grid[i][0] == one:
            dp[i][0] = 1
            ans = 1
    for i in range(1,rows):
        for j in range(1,cols):
            if grid[i][j] == 1:
                dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                ans = max(ans,dp[i][j])
    return ans

