from collections import defaultdict,deque
import heapq

def calcCost(src,dest):
    return abs(src[0] - dest[0]) + abs(src[1] - dest[1])
    
def minCost(points):
    graph = defaultdict(list)
    n = len(points)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            graph[i].append((calcCost(points[i],points[j]),j))
    
    
    pq = []
    ans = 0
    visited = defaultdict(bool)
    heapq.heappush(pq,(0,i))
    while pq:
        cost,node = heapq.heappop(pq)
        if visited[node]:
            continue
        ans += cost
        visited[node] = True
        for c,nbr in graph[node]:
            if not visited[nbr]:
                heapq.heappush(pq,(c,nbr))
    return ans

arr = [[0,0]]
print(minCost(arr))  

            