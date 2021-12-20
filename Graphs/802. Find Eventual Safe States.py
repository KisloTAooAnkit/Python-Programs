from bisect import bisect_left
from collections import defaultdict,deque
def sol(graph):
    terminals = []
    termL = 0
    n = len(graph)
    outDegree = [0]*n
    for node,nbrs in enumerate(graph):
        val = len(nbrs)
        if val == 0:
            terminals.append(node)
            termL +=1
        outDegree[node] = val
    ans = []
    for node,nbrs in enumerate(graph):
        termCount = 0
        if outDegree[node] > termL:
            continue
        for terminal in terminals:
            val = bisect_left(nbrs,terminal)
            if val < outDegree[node] and nbrs[val] == terminal:
                termCount +=1
        
        if outDegree[node] == termCount:
            ans.append(node)
    return ans

def safeState(graph):
    n = len(graph)
    revGraph = defaultdict(list)
    outDegree = [0]*n
    q = deque()
    for node in range(n):
        c = 0
        for nbr in graph[node]:
            revGraph[nbr].append(node)
            c +=1
        outDegree[node] = c
        if c == 0:
            q.append(node)
    ans = []
    while q:
        node = q.popleft()
        ans.append(node)
        for nbr in revGraph[node]:
            outDegree[nbr] -=1
            if outDegree[nbr] == 0:
                q.append(nbr)
    return sorted(ans)



graph = [[],[0,2,3,4],[3],[4],[]]
print(safeState(graph))
        
            