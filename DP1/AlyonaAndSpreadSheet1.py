def fillROWDP(rowDP,matrix,rows,cols):
    
    for col in range(cols):
        currentStreak = 1
        for row in range(1,rows):
            if matrix[row-1][col] <= matrix[row][col]:
                currentStreak +=1
            else:
                currentStreak = 1
            rowDP[row] = max(rowDP[row],currentStreak)
                      

 
def startPoint():
    rows,cols = list(map(int,input().strip().split()))
    matrix = []
    for i in range(rows):
        matrix.append([int(j) for j in input().split()])
    rowDp= [1]*rows
    fillROWDP(rowDp,matrix,rows,cols)
    qryCount = int(input())
    while(qryCount):
        left,right = list(map(int,input().strip().split()))
        ans = rowDp[right-1] >= (right - left +1) 
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
# dp = [1]*rows
# fillROWDP(dp,matrix,rows,cols)
startPoint()