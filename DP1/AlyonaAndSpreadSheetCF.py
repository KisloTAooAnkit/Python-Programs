def prepareDP(matrix,row,col,dp,rowDp):
    for j in range(col):
        prev = float("inf")
        for i in range(row):
            if prev > matrix[i][j]:
                dp[i][j] = 1
                prev = matrix[i][j]
                
            else:
                dp[i][j] = dp[i-1][j] + 1
                prev = matrix[i][j]
            rowDp[i] = max(rowDp[i],dp[i][j])

def solution(rowDp,left,right):
    qr = right-left + 1
    if rowDp[right-1] >= qr:
        return True
    else:
        return False


def startPoint():
    rows,cols = list(map(int,input().strip().split()))
    matrix = []
    for i in range(rows):
        matrix.append([int(j) for j in input().split()])
    dp = [[0 for i in range(cols)] for i in range(rows)]
    rowDp= [0]*rows
    prepareDP(matrix,rows,cols,dp,rowDp)
    qryCount = int(input())
    while(qryCount):
        left,right = list(map(int,input().strip().split()))
        ans = solution(rowDp,left,right)
        print("Yes" if ans else "No")
        qryCount-=1
# rows = 5
# cols = 4

# matrix = [
#     [1 ,2, 3 ,5],
#     [3 ,1 ,3 ,2],
#     [4 ,5 ,2 ,3],
#     [5 ,5 ,3 ,2],
#     [4 ,4 ,3 ,4]
#     ]
# dp = [[0 for i in range(cols)] for i in range(rows)]
# prepareDP(matrix,rows,cols,dp)

startPoint()

