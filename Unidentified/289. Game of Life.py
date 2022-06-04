class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        
        dir = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        
        for row in range(n):
            for col in range(m):
                liveC = 0
                for dx,dy in dir:
                    newR = row + dx
                    newC = col + dy
                    
                    if newR <0 or newR == n or newC < 0 or newC == m:
                        continue
                    if board[newR][newC]%2 == 1:
                        liveC +=1
                
                if board[row][col] == 1:
                    if liveC == 2 or liveC == 3:
                        board[row][col] = 3
                    else:
                        board[row][col] = 1
                else:
                    if liveC == 3:
                        board[row][col] = 2
                    else:
                        board[row][col] = 0
        
        for i in range(n):
            for j in range(m):
                if board[i][j] >1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
                    