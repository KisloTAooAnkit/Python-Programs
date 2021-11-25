def maxSquare(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    ans = 0
    #fill boundary
    for i in range(cols):
        if matrix[0][i] == "1":
            dp[0][i] = 1
    for i in range(rows):
        if matrix[i][0] == "1":
            dp[i][0] = 1
            
  
    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][j] == "1":
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                ans= max(dp[i][j],ans)
    return ans