def maxSumRectangle(matrix):
    row = len(matrix)
    col = len(matrix[0])
    
    prefixSum = [[0 for _ in range(col)] for _ in range(row)]
    
    prefixSum[row-1][col-1] = matrix[row-1][col-1]
    
    #fix last row
    prev = prefixSum[row-1][col-1]
    for j in range(col-2,-1,-1):
        prefixSum[row-1][j] = matrix[row-1][j] + prev
        prev = prefixSum[row-1][j]
    #fix last col
    prev = prefixSum[row-1][col-1]
    for i in range(row-2,-1,-1):
        prefixSum[i][col-1] = matrix[i][col-1] + prev 
        prev = prefixSum[i][col-1]
    #fill rest of matrix sum
    for i in range(row-2,-1,-1):
        for j in range(col-2,-1,-1):
            prefixSum[i][j] = prefixSum[i+1][j] + prefixSum[i][j+1] - prefixSum[i+1][j+1]
    
    #find maxrect
    globalmax = float("-inf")
    for i in range(0,row):
        for j in range(0,col):
            start = prefixSum[i][j]
            for k in range(0,row):
                for l in range(0,col):
                    if k < row-1:
                        start -= prefixSum[k+1][j]
                    if l < col-1:
                        start -= prefixSum[i][l+1]
                    if l < col-1 and k < row-1:
                        start += prefixSum[k+1][l+1]
                    globalmax = max(globalmax,start)
    return globalmax                    
    
    
    