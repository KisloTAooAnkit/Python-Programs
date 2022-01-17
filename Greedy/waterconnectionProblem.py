from collections import defaultdict
import re

def dfs(graph,src,ans):
    if len(graph[src])==0:
        return src
    
    for nbr,cost in graph[src]:
        ans[0] = min(ans[0],cost)
        return dfs(graph,nbr,ans)



def waterConnectionProblem(n,p,a,b,d):

    graph = defaultdict(lambda : [])
    indgree = defaultdict(lambda : 0)

    for i in range(p):
        src = a[i]
        dest = b[i]
        cost = d[i]
        graph[src].append((dest,cost))
        if src not in indgree:
            indgree[src] = 0

        indgree[dest] +=1
    res = []
    startPoints = [key for key in indgree if indgree[key] == 0 ]
    ans = [0]
    for src in startPoints:
        ans[0] = float("inf")
        dst = dfs(graph,src,ans)
        res.append([src,dst,ans[0]])

    return res

n = 17
p = 11
g = [(6,5,2),(4,7,2),(14,16,2),(3,2,8),(17,12,4),(15,13,2),(16,6,8),(5,17,8),(7,1,9),(11,4,9),(12,8,2)]
a = [i[0] for i in g]
b = [i[1] for i in g]
d = [i[2] for i in g]

res = waterConnectionProblem(n,p,a,b,d)
print(res)