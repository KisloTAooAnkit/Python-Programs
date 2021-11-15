def maxSquaresOfOnes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    prefixSum = [[0 for _ in range(cols)] for _ in range(rows)]

    prefixSum[rows-1][cols-1] = int(matrix[rows-1][cols-1])
    prev = prefixSum[rows-1][cols-1]
    for j in range(cols-2,-1,-1):
        prefixSum[rows-1][j] = int(matrix[rows-1][j]) + prev
        prev = prefixSum[rows-1][j]
    #fix last col
    prev = prefixSum[rows-1][cols-1]
    for i in range(rows-2,-1,-1):
        prefixSum[i][cols-1] = int(matrix[i][cols-1]) + prev 
        prev = prefixSum[i][cols-1]
    #fill rest of matrix sum
    for i in range(rows-2,-1,-1):
        for j in range(cols-2,-1,-1):
            prefixSum[i][j] = int(matrix[i][j]) + prefixSum[i+1][j] + prefixSum[i][j+1] - prefixSum[i+1][j+1]

    print(prefixSum)
    ans = 0
    for row in range(0,rows):
        for col in range(cols):
            if int(matrix[row][col]) == 0:
                continue
            diagx,diagy = row,col
            while(diagx<rows and diagy<cols):
                sumofthisBlock = prefixSum[row][col]
                if diagy +1 < cols:
                    sumofthisBlock -= prefixSum[row][diagy+1]
                if diagx +1 <rows:
                    sumofthisBlock -= prefixSum[diagx+1][col]
                if diagx +1 < rows and diagy +1 < cols:
                    sumofthisBlock += prefixSum[diagx+1][diagy+1]

                shouldBeSumOfThisBlock = (diagy - col + 1)**2
                if shouldBeSumOfThisBlock == sumofthisBlock:
                    ans= max(sumofthisBlock,ans)
                else:
                    break
                diagy+=1
                diagx+=1
    return ans

grid = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]
print(maxSquaresOfOnes(grid))

                
