from collections import defaultdict as dict,deque


def bfs(graph):
    q = deque()
    visited = dict(bool)
    shortestDist = dict(int)
    visited[1] = True
    shortestDist[1] = 0
    q.append(1)
    while(q):
        node = q.popleft()
        for newNode in graph[node]:
            if newNode not in visited:
                q.append(newNode)
                visited[newNode] = True
                shortestDist[newNode] = shortestDist[node] +1
            if newNode == 30:
                return shortestDist[30]

def constructGraph(snakes,ladders):
    graph = dict(list)
    snakeMap = dict(int)
    laddersMap = dict(int)
    
    for src,dest in snakes:
        snakeMap[src] = dest
    for src,dest in ladders:
        laddersMap[src] = dest

    n = 31
    for i in range(1,n):
        l = [i+1,i+2,i+3,i+4,i+5,i+6]
        for val in l:
            if val in snakeMap:
                graph[i].append(snakeMap[val])
            elif val in laddersMap:
                graph[i].append(laddersMap[val])
            elif val < n:
                graph[i].append(val)

    #print(graph)
    return graph

def findShortestPath(snakes,ladders):
    graph = constructGraph(snakes,ladders)
    return bfs(graph)


ladders = [
    (11,26),
    (3,22),
    (5,8),
    (20,29)
]

snakes = [
    (29,1),
    (21,9),
    (17,4),
    (19,7)
]

print("Minimum Number of dice roles : {0}".format(findShortestPath(snakes,ladders)))