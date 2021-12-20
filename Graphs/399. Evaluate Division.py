from collections import defaultdict,deque
from typing import Text

def dfs(graph,src,dest,ans,visited):
    if src not in graph or dest not in graph:
        return False
    if src == dest:
        return True

    visited[src]= True
    for nbr,cost in graph[src]:
        if visited[nbr]:
            continue
        cache = ans[0]
        ans[0] = ans[0]*cost
        if(dfs(graph,nbr,dest,ans,visited)):
            visited[src] = False
            return True
        ans[0] = cache
    visited[src] = False
    return False

def ans(equations,values,queries):
    graph = defaultdict(list)
    visited = defaultdict(bool)
    for idx,val in enumerate(equations):
        graph[val[0]].append((val[1],values[idx]))
        graph[val[1]].append((val[0],1/values[idx]))
    res = []
    for src,dest in queries:
        ans = [1]
        if dfs(graph,src,dest,ans,visited):
            res.append(ans[0])
        else:
            res.append(-1)
    return res        

equations =  [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(ans(equations,values,queries))