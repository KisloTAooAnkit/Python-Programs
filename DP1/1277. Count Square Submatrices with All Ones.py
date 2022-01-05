def countSq(matrix):
    r = len(matrix)
    c = len(matrix[0])
    
    dp = [[0]*c for _ in range(r)]
    
    for i in range(r-1,-1,-1):
        for j in range(c-1,-1,-1):
            col = j+1
            row = i+1
            v1,v2,v3 = 0,0,0
            
            if row < r:
                v1 = dp[row][j]
            if col < c:
                v2 = dp[i][col]
            
            if row < r and col < c:
                v3 = dp[row][col]
                
            dp[i][j] = matrix[i][j] + v1 + v2 - v3
    ans = 0
    for i in range(r):
        for j in range(c):
            row = i
            col = j
            while(row<r and col<c):
                rr = row+1
                cc = col+1
                v1,v2,v3 = 0,0,0
                if rr < r:
                    v1 = dp[rr][j]
                if cc < c:
                    v2 = dp[i][cc]
                if rr<r and cc<c:
                    v3 = dp[rr][cc]
                
                val = dp[i][j] - v1 - v2 + v3
                if val == (row-i +1)*(col-j+1):
                    ans += 1
                row +=1
                col+=1
    return ans
    
matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

print(countSq(matrix))