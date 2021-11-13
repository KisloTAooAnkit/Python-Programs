import sys

def minCost(matrix,si,sj,ei,ej,maxrow,maxcol):
    if(si == ei and sj == ej):
        return matrix[si][sj]
    
    if(si>=maxrow or sj>=maxcol or si < 0 or sj < 0):
        return sys.maxsize 
    
    ans = matrix[si][sj]
    res1 = minCost(matrix,si+1,sj,ei,ej,maxrow,maxcol)
    res2 = minCost(matrix,si,sj+1,ei,ej,maxrow,maxcol)
    res3 = minCost(matrix,si+1,sj+1,ei,ej,maxrow,maxcol)
    
    return ans + min(res1,res2,res3)
    

def minCostDP(matrix,si,sj,ei,ej,maxrow,maxcol,dp):
    if(si == ei and sj == ej):
        return matrix[si][sj]
    
    if(si>=maxrow or sj>=maxcol or si < 0 or sj < 0):
        return sys.maxsize 
    
    
    if(dp[si][sj] != -1):
        return dp[si][sj]
    
    ans = matrix[si][sj]
    res1 = minCostDP(matrix,si+1,sj,ei,ej,maxrow,maxcol,dp)
    res2 = minCostDP(matrix,si,sj+1,ei,ej,maxrow,maxcol,dp)
    res3 = minCostDP(matrix,si+1,sj+1,ei,ej,maxrow,maxcol,dp)

    ans += min(res1,res2,res3)    
    dp[si][sj] = ans
    return ans


def caller (matrix,ei,ej):
    row = len(matrix)
    col = len(matrix[0])
    dp = [[-1 for j in range(col)] for i in range(row)]
    return minCostDP(matrix,0,2,ei,ej,row,col,dp)



maze = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
        ]

print(caller(maze,2,2))