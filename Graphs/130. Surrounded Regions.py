
def helper(board,i,j,m,n,visited,pathArr):
    
    if i >= m or i < 0 or j >= n or j < 0:
        return False
    if visited[i][j] == 1 and board[i][j] =="O":
        return False
    if board[i][j] == "X":
        return True
    
    visited[i][j] = 1
    board[i][j] = "X"
    pathArr.append((i,j))
    ans1 = helper(board,i+1,j,m,n,visited,pathArr)
    ans2 = helper(board,i-1,j,m,n,visited,pathArr)
    ans3 = helper(board,i,j+1,m,n,visited,pathArr)
    ans4 = helper(board,i,j-1,m,n,visited,pathArr)
    res = ans4 and ans3 and ans2 and ans1
    if not res:
        while pathArr:
            x,y = pathArr.pop()
            board[x][y] = "O"
    return res
    
"""---------------------------Boundary Traversal ----------------------"""


def MarkDFS(board,i,j,m,n):
    if i >= m or i < 0 or j >= n or j < 0:
        return 
    if board[i][j] == "O":
        board[i][j] == 1
        MarkDFS(board,i+1,j,m,n)
        MarkDFS(board,i-1,j,m,n)
        MarkDFS(board,i,j+1,m,n)
        MarkDFS(board,i,j-1,m,n)
    return

def solveWithBoundary(board):
    rows = len(board)
    cols = len(board[0])

    for j in range(cols):
        MarkDFS(board,0,j,rows,cols)
        MarkDFS(board,rows-1,j,rows,cols)
    for i in range(rows):

        MarkDFS(board,i,0,rows,cols)
        MarkDFS(board,i,cols-1,rows,cols)

            
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                board[i][j] == "O"
            if board[i][j] == "O":
                board[i][j] == "X"
    
    
    

def solve(board):
    m = len(board)
    n = len(board[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    pathArr = []
    for i in range(m):
        for j in range(n):
            if board[i][j] == "O" and visited[i][j] == 0:
                helper(board,i,j,m,n,visited,pathArr)
                pathArr.clear()
    print(board)
    
board = [
    ["X","X","X","X"],
    ["X","O","X","O"],
    ["X","O","X","X"],
    ["X","X","X","X"]
    ]

solve(board)