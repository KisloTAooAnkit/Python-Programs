from collections import deque
def multiSourceBFS(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    minDist = [[float("inf")]*cols for _ in range(rows)]
    q = deque()
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                minDist[i][j] = 0
                q.append((i,j))
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            destX = x + dx[i]
            destY = y + dy[i]
            if destX >= 0 and destY >= 0 and destY < cols and destX < rows and minDist[destX][destY] == float("inf"):
                minDist[destX][destY] = 1 + minDist[x][y]
                q.append((destX,destY))

    
    for row in minDist:
        print(row)
    
    
grid = [[0,0,0,0,0,0],
        [0,1,1,0,1,0],
        [0,0,0,0,0,0],
        [0,0,0,0,1,0],
        [0,0,1,0,0,0],
        [1,0,0,0,0,1]
        ]

multiSourceBFS(grid)

    