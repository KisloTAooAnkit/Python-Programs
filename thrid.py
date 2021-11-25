def maxSq(n,m,matrix):
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        if matrix[0][i] == 1:
            dp[0][i] = 1
    for j in range(n):
        if matrix[j][0] == 1:
            dp[j][0] = 1

    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j] == 1:
                dp[i] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j]) + 1
    return dp[n-1][m-1]