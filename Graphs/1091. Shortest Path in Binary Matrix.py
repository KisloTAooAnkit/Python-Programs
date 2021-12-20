from collections import deque
def shortestPathInBinMatrix(grid):
    ans = 0
    row = len(grid)
    col = len(grid[0])    
    q = deque()
    qSize = 0
    if grid[0][0] == 0:
        qSize +=1
        q.append((0,0))
    
    dx = [(-1,0),
          (0,1),
          (1,0),
          (0,-1),
          (1,1),
          (1,-1),
          (-1,1),
          (-1,-1)
          ]
    
    while q:
        for i in range(qSize):
            x,y = q.popleft()
            qSize -=1
            if x == row -1 and y == col -1:
                return ans
            for i in range(8):
                pair = dx[i]
                xx = x + pair[0]
                yy = y + pair[1]
                if xx >=0 and yy>=0 and xx<row and yy<col and grid[xx][yy] != 1:
                    grid[xx][yy] = 1
                    q.append((xx,yy))
                    qSize +=1
        ans +=1
    return -1