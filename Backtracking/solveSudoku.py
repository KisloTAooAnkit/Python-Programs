

n = 9

def hasEmptyLocation(grid,row,col):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == ".":
                row[0] = i
                col[0] = j
                return True
    return False

def isSafeInRow(grid,row,col,num):
    for i in range(n):
        if grid[row[0]][i] == num:
            return False
    return True
    
def isSafeInCol(grid,row,col,num):
    for i in range(n):
        if grid[i][col[0]] == num:
            return False
    return True
    
def isSafeInGrid(grid,row,col,num):
    rowfactor = row[0] - (row[0]%3)
    colfactor = col[0] - (col[0]%3)
    for i in range(rowfactor,rowfactor+3):
        for j in range(colfactor,colfactor+3):
            if grid[i][j] == num:
                return False
    return True
    
def isSafe(grid,row,col,num):
    return (
        isSafeInCol(grid,row,col,num) and 
        isSafeInRow(grid,row,col,num) and 
        isSafeInGrid(grid,row,col,num)
        )

def solveSudoku(grid):
    row,col = [0],[0]
    # find empty slot if no empty slot present in board then we have ans
    if not hasEmptyLocation(grid,row,col): 
        return True
    #hit and try for every number to place in that slot 
    for i in range(1,10):
        if isSafe(grid,row,col,i):
            grid[row[0]][col[0]] = 1
            if(solveSudoku(grid)):
                return True #early return as we have to stop even if we get even 1 ans
            grid[row[0]][col[0]] = 0
    return False
