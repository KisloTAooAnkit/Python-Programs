def miserMan(grid,rows,cols):
    dp = [[0 for _ in range(cols)] for _ in range(2)]
    flag = 1
    for j in range(cols):
        dp[flag][j] = grid[rows-1][j]
    
    for i in range(rows-2,-1,-1):
        for j in range(cols):
            if j == cols-1:
                dp[flag^1][j] = grid[i][j] + min(dp[flag][j],dp[flag][j-1])
            elif j == 0:
                dp[flag^1][j] = grid[i][j] + min(dp[flag][j],dp[flag][j+1])
            else:
                dp[flag^1][j] = grid[i][j] + min(dp[flag][j],dp[flag][j-1],dp[flag][j+1])
        flag = 1 - flag
    ans = float("inf")
    for j in range(cols):
        
        ans = min(ans,dp[flag][j])
    return ans

rows,cols = list(map(int,input().strip().split()))
matrix = []
for i in range(rows):
   col = list(map(int, input().split()))
   matrix.append(col)
print(miserMan(matrix,rows,cols))



# matrix = [
#     [1,3,1,2,6],
#     [10,2,5,4,15],
#     [10,9,6,7,1],
#     [2,7,1,5,3],
#     [8,2,6,1,9]    
#           ]
# n = len(matrix)
# m = len(matrix[0])
# print(miserMan(matrix,n,m))