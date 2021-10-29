def helper(matrix,visited,ans,path,i,j,n):
    if ((i >=n or j >= n)  or (i < 0 or j < 0)):
        return        
    if matrix[i][j] == 0 or visited[i][j] == 1:
        return 
    if i == n-1 and j == n-1:
        ans.append(path)
        return
    
    visited[i][j] = 1
    helper(matrix,visited,ans,path+"R",i,j+1,n)
    helper(matrix,visited,ans,path+"L",i,j-1,n)
    helper(matrix,visited,ans,path+"U",i-1,j,n)
    helper(matrix,visited,ans,path+"D",i+1,j,n)
    visited[i][j] = 0
    return 
    


def ratInMaze(matrix,n):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    i = 0
    j = 0
    path = ""
    ans = []
    helper(matrix,visited,ans,path,i,j,n)
    ans.sort()
    return ans


matrix = [
        [1,0,0,0],
        [1,1,0,1],
        [1,1,0,0],
        [0,1,1,1]
        ]
n = len(matrix)

print(ratInMaze(matrix,n))