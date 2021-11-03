from collections import deque

def orangesRotting(grid):
    q = deque()
    totalOranges = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                q.append((i,j))
                totalOranges +=1
            if grid[i][j] == 1:
                totalOranges +=1
    
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    days = 0
    hasInfected = False
    rottenOrangeCount = 0
    while q:
        currentRottenOranges = len(q) 
        rottenOrangeCount += currentRottenOranges
        while(currentRottenOranges):
            x,y = q.popleft()
            for i in range(4):
                freshRow = x + dx[i]
                freshCol = y + dy[i]
                if freshRow < 0 or freshRow >= rows or freshCol>=cols or freshCol<0 or grid[freshRow][freshCol] != 1:
                    continue
                grid[freshRow][freshCol] = 2
                hasInfected = True
                q.append((freshRow,freshCol))
            currentRottenOranges-=1
        if hasInfected:
            hasInfected = False
            days +=1
    
    return days if rottenOrangeCount == totalOranges else -1
    

    

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))