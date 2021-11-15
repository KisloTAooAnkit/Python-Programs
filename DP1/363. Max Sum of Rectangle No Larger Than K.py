import sys
def kadanesModified(arr,k):
    globalmax = -sys.maxsize
    runningSum = -sys.maxsize
    for i in range(0,len(arr)):
        runningSum = max(arr[i]+runningSum,arr[i])
        if globalmax < runningSum <=k:
            globalmax = runningSum
    return globalmax
        

def maximalAreaRectDP(matrix,k):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [0] * rows
    ans = -sys.maxsize
    for point1 in range(cols):
        for row in range(rows):
            dp[row] = matrix[row][point1] 
        
        for point2 in range(point1,cols):
            if point1 == point2:
                ans = max(ans,kadanesModified(dp,k))
                continue
            for row in range(rows):
                 dp[row] += matrix[row][point2]
            
            ans = max(ans,kadanesModified(dp,k))
    return ans 
                
grid =[
    [5,-4,-3,4],
    [-3,-4,4,5],
    [5,1,5,-4]
       ]

k = 8
print(maximalAreaRectDP(grid,k))