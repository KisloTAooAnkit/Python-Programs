from collections import deque
def findShortestPath(grid):
    r = len(grid)
    c = len(grid[0])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    ans = 0
    qSize = 0
    q = deque()
    for i in range(c):
        if grid[0][i] == 1:
            grid[0][i] = 0
            q.append((0,i))
            qSize +=1
            
    
    while q:
        for i in range(qSize):
            x,y = q.popleft()
            qSize -=1
            if x == r -1:
                return ans
            for j in range(4):
                xx = x + dx[j]
                yy = y + dy[j]
                
                if xx >=0 and yy>=0 and xx<r and yy<c and grid[xx][yy]!=0:
                    q.append((xx,yy))
                    grid[xx][yy] = 0
                    qSize +=1
        ans +=1

grid = [[0,1,0,0,1,0],
        [0,1,1,0,1,0],
        [0,1,1,1,0,1],
        [1,1,1,1,1,1],
        [1,0,1,0,0,1],
        [0,0,0,0,0,1]]

print(findShortestPath(grid))