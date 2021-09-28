import sys
# def minPathSum(grid) -> int:
#     row = len(grid)
#     col = len(grid[0])

#     dp = [[-1 for j in range(col)] for i in range(row)]
#     test = [[-1 for j in range(col)] for i in range(row)]
#     for i in range(row):
#         for j in range(col):
#             test[i][j] = grid[i][j]

#     minCostDP(grid,0,0,row-1,col-1,row,col,dp,test)
    
#     print(grid)
    
#     dp = [[-1 for j in range(col)] for i in range(row)]
    
#     ans = minCostDP1(grid,0,0,row-1,col-1,row,col,dp)
    
#     return ans - test[row-1][col-1]

# def minCostDP(matrix,si,sj,ei,ej,maxrow,maxcol,dp,glob):

#     if(si == ei and sj == ej):
#         return matrix[si][sj]

#     if(si>=maxrow or sj>=maxcol or si < 0 or sj < 0):
#         return -sys.maxsize 


#     if(dp[si][sj] != -1):
#         return dp[si][sj]

#     ans = matrix[si][sj]
#     matrix[si][sj] = 0
#     res1 = minCostDP(matrix,si+1,sj,ei,ej,maxrow,maxcol,dp,glob)
#     res2 = minCostDP(matrix,si,sj+1,ei,ej,maxrow,maxcol,dp,glob)

#     if res1>res2:
#         if si <= ei and sj+1 <=ej:
#             matrix[si][sj+1] = glob[si][sj+1]
#         ans += res1
#     else:
#         if si+1 <= ei and sj <=ej:
#             matrix[si+1][sj] = glob[si+1][sj]
#         ans += res2
#     dp[si][sj] = ans
#     return ans


# def minCostDP1(matrix,si,sj,ei,ej,maxrow,maxcol,dp):

#     if(si == ei and sj == ej):
#         return matrix[si][sj]

#     if(si>=maxrow or sj>=maxcol or si < 0 or sj < 0):
#         return -sys.maxsize 


#     if(dp[si][sj] != -1):
#         return dp[si][sj]

#     ans = matrix[si][sj]
#     res1 = minCostDP1(matrix,si+1,sj,ei,ej,maxrow,maxcol,dp)
#     res2 = minCostDP1(matrix,si,sj+1,ei,ej,maxrow,maxcol,dp)

#     ans += max(res1,res2)
#     dp[si][sj] = ans
#     return ans

a = [
    [20,3,20,17,2,12,15,17,4,15],
    [20,10,13,14,15,5,2,3,14,3]
    ]

def ans(a):
    row = len(a[0])
    pf1 = [0]*(row)
    pf2 = [0]*(row)
    prev = 0
    for i in range(row):
        pf1[i] = a[0][i] + prev
        prev = pf1[i]
    prev = 0
    for i in range(row-1,-1,-1):
        pf2[i] = a[1][i] + prev
        prev = pf2[i]
        
    print(pf1)
    print(pf2)
    maxi = -1
    res = -sys.maxsize
    for i in range(0,row):
        if pf1[i] + pf2[i] > res:
            res = pf1[i] + pf2[i]
            maxi = i
    
    for i in range(0,maxi+1):
        pf1[i] = 0

    for j in range(maxi,row):
        pf2[j] = 0 
        
    print(pf1)
    print(pf2)


print(ans(a))