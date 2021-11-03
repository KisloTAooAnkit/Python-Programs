

def isPossible(x,y,matrix,n):
    #checking column
    for i in range(x-1,-1,-1):
        if matrix[i][y] == "Q":
            return False
    
    #checking right upper diagonal
    i = x-1
    j = y+1
    while(i>-1 and j < n):
        if matrix[i][j] == "Q":
            return False
        i -=1
        j +=1
    
    #checking Left upper diagonal
    i = x-1
    j = y-1
    while(i>-1 and j > -1):
        if matrix[i][j] == "Q":
            return False
        i -=1
        j -=1
    return True
    
def prepareAns(matrix,ans):
    ls = []
    for row in matrix:
        ls.append("".join(row))
    print(ls)
    ans.append(ls)
    print("----------------")
    
def NQueensHelper(row,matrix,n,ans):
    if row == n:
        prepareAns(matrix,ans)
        return
    for col in range(n):
        if isPossible(row,col,matrix,n):
            matrix[row][col] = "Q"
            NQueensHelper(row+1,matrix,n,ans)
            matrix[row][col] = "."
    return

def NQueens(n):
    matrix = [["." for _ in range(n)] for j in range(n)]
    ans = []
    NQueensHelper(0,matrix,n,ans)

    

n = 4
NQueens(n)