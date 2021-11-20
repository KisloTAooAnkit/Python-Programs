import sys
import bisect


def slidingWindow(arr,k,n):
    dp = dict()
    dp[0] = 1
    prevSum = 0
    ans = -sys.maxsize
    for i in range(n):
        prefixSumTillNow = prevSum + arr[i]
        redundantSum = prefixSumTillNow - k
        start = redundantSum
        end = prefixSumTillNow
        pass               


        

def maximalAreaRectDP(matrix,k):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [0] * rows
    ans = -sys.maxsize
    for point1 in range(cols):
        for row in range(rows):
            dp[row] = 0
        for point2 in range(point1,cols):
            for row in range(rows):
                 dp[row] += matrix[row][point2]
            
            ans = max(ans,slidingWindow(dp,k,rows))
    return ans 
                
grid =[[2,2,-1]]
k = 0
print(maximalAreaRectDP(grid,k))