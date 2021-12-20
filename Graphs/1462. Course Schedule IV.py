from collections import defaultdict,deque
def checkPreq(n,preq,queries):
    
    graph = [[0]*n for _ in range(n)]    
    for s,d in preq:
        graph[s][d] = 1
    
    queryMat = [[0]*n for _ in range(n)]
    indegree = [0]*n
    
    for i in range(n):
        for j in range(n):
            indegree[j] += graph[i][j]
    
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        for nbr in range(n):
            if graph[node][nbr] != 1:
                continue
            indegree[nbr] -=1
            if indegree[nbr] == 0:
                q.append(nbr)
            for col in range(n):
                if queryMat[node][col] == 1:
                    queryMat[nbr][col] = 1
            queryMat[nbr][node] = 1
    ans = []
    for s,d in queries:
        if queryMat[d][s] == 1:
            ans.append(True)
        else:
            ans.append(False)
    return ans 

    
numCourses = 4
prerequisites =[[2,3],[2,1],[0,3],[0,1]]
queries =[[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]]

print(checkPreq(numCourses,prerequisites,queries))