from collections import defaultdict as dict,deque


def BFS(edges,sv,n,alreadyInQ):
    q = deque()
    q.append(sv)
    alreadyInQ[sv] = 1
    while q:
        val = q.popleft()
        print(val)
        for i in range(n):
            if i == val or i in alreadyInQ:
                continue
            if edges[val][i]:
                q.append(i)
                alreadyInQ[i] = 1
            
                        

def createGraph():
    n = int(input())
    e = int(input())
    edges = [[False]*(n+1) for _ in range(n+1)]

    for i in range(e):
        f,s = list(map(int,input().strip().split()))
        edges[f][s] = True
        edges[s][f] = True
    visited = dict(int)
    BFS(edges,0,n,visited)

createGraph()