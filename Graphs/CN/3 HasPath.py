from collections import defaultdict as dict
def checkPath(edges,n,sv,visited,ev):
    if sv == ev:
        return True
    visited[sv] = 1
    for i in range(n):
        if i == sv:
            continue
        if edges[sv][i] and i not in visited:
            return checkPath(edges,n,i,visited,ev)
    return False

def checkPathDFS(start,end,n,graph):
    visited = dict(int)
    return checkPath(graph,n,start,visited,end)  


def createGraph():
    n = int(input("Enter number of vertices : "))
    e = int(input("Enter number of edges : "))
    graph = [[False]*(n+1) for _ in range(n+1)]

    for i in range(e):
        f,s = list(map(int,input("Enter Path : ").strip().split()))
        graph[f][s] = True
        graph[s][f] = True
    
    queries = int(input("Enter number of queries : "))
    for i in range(queries):
        start,end = list(map(int,input("Enter Start and End : ").strip().split()))
        print(checkPathDFS(start,end,n,graph))

createGraph()