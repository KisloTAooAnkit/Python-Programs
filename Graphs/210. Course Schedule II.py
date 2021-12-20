from collections import defaultdict,deque

def findOrder(n,preq):
    
    if len(preq) == 0:
        return [i for i in range(n)]
    
    graph = defaultdict(list)
    for d,s in preq:
        graph[s].append(d)

    indegree = defaultdict(int)
    for node in graph:
        if node not in indegree:
            indegree[node] = 0
        for nbrs in graph[node]:
            indegree[nbrs] +=1
    
    q = deque()
    remainingCourses = n
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
    ans = []
    while(q):
        node = q.popleft()
        remainingCourses -=1
        ans.append(node)
        for nbr in graph[node]:
            indegree[nbr] -=1
            if indegree[nbr] == 0:
                q.append(nbr)
    
    if remainingCourses == 0:
        return ans
    else:
        return []

prerequisites = []
numCourses = 1
print(findOrder(numCourses,prerequisites))