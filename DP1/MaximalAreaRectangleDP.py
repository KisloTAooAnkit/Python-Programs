def kadanes(arr):
    globalMax = arr[0]
    runningSum = arr[0]
    for i in range(1,len(arr)):
        runningSum = max(arr[i]+runningSum,arr[i])
        globalMax = max(globalMax,runningSum)
    return globalMax
        


def maximalAreaRectDP(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [0] * rows
    ans = float("-inf")
    for point1 in range(cols):
        for row in range(rows):
            dp[row] = matrix[row][point1] 
        
        for point2 in range(cols):
            if point1 == point2:
                continue
            for row in range(rows):
                 dp[row] += matrix[row][point2]
            
            ans = max(ans,kadanes(dp))
    return ans 
                
            