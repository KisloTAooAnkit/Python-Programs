def uniquePaths(rows,cols):
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    dp[rows-1][cols-1] = 1
    
    for i in range(0,rows):
        dp[i][cols-1] = 1
    
    for j in range(cols):
        dp[rows-1][j] = 1
    
    for i in range(rows-1,-1,-1):
        for j in range(cols-1,-1,-1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]
    return dp[0][0]
    