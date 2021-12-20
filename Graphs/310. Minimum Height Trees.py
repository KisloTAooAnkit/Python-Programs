from collections import deque,defaultdict

def sol(n,edges):
    
    if n<=2:
        return [i for i in range(n)]
    
    graph = defaultdict(list)
    
    for src,d in edges:
        graph[src].append(d)
        graph[d].append(src)
    
    indgree = defaultdict(int)
    
    for node in graph:
        #indgree[node] +=1
        for nbr in graph[node]:
            indgree[nbr] +=1
    
    q = deque()
    ans = []
    for node in indgree:
        if indgree[node] == 1:
            q.append(node)
    
    remainingNodes = n
    
    while remainingNodes > 2:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            remainingNodes -=1
            indgree[node] -=1
            for nbr in graph[node]:
                indgree[nbr] -=1
                if indgree[nbr] == 1:
                    q.append(nbr)
    ans = []
    while q:
        ans.append(q.popleft())
    return ans
edges = [[0,1]]
n = 2
print(sol(n,edges))