
def dfs(color,grid,i,j,rows,cols):
    if i < 0 or j<0 or i==rows or j == cols or grid[i][j] != 1:
        return 0
    
    grid[i][j] = color
    
    up = dfs(color,grid,i-1,j,rows,cols)
    down = dfs(color,grid,i+1,j,rows,cols)
    left = dfs(color,grid,i,j-1,rows,cols)
    right = dfs(color,grid,i,j+1,rows,cols)
    
    return 1 + up + down + left + right
    
#checking all 4 directional colors
def calcMaxArea(grid,i,j,rows,cols,dic):
    
    colorMap = dict()
    
    if i-1 >-1 and grid[i-1][j] != 0:
        up = grid[i-1][j]
        colorMap[up] = dic[up]    
    
    if i+1 < rows and grid[i+1][j] != 0:
        down = grid[i+1][j]
        colorMap[down] = dic[down] 
        
    if j-1 > -1 and grid[i][j-1] !=0:
        left = grid[i][j-1]
        colorMap[left] = dic[left]
    
    if j+1 < cols and grid[i][j+1] != 0:
        right = grid[i][j+1]
        colorMap[right] = dic[right]
    
    ans = 1
    for key in colorMap:
        ans += colorMap[key]
    return ans


def sol(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    color = 2
    dic = dict()
    ans = 0
    #precomputing and marking 1 blobs with diffrent colors
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                res = dfs(color,grid,i,j,rows,cols)
                dic[color] = res
                color +=1
                
    #selecting zero one by one
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                res = calcMaxArea(grid,i,j,rows,cols,dic)
                ans = max(ans,res)
    return ans


grid =  [[1,1],[1,0]]
print(sol(
 grid   
))