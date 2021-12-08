from collections import defaultdict as dict

def printEdge(edges,n,sv,visited):
    print(sv)
    visited[sv] = 2
    for i in range(n):
        if i == sv:
            continue
        if edges[sv][i] and visited[i] !=2:
            printEdge(edges,n,i,visited)
    
def createGraph():
    n = int(input())
    e = int(input())
    edges = [[False]*(n+1) for _ in range(n+1)]

    for i in range(e):
        f,s = list(map(int,input().strip().split()))
        edges[f][s] = True
        edges[s][f] = True
    visited = dict(int)
    printEdge(edges,n,0,visited)

createGraph()