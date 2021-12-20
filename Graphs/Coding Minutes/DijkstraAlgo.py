
from collections import defaultdict
import heapq as heap

def dijkstra(graph, startingNode):
    
    distance = defaultdict(lambda : float("inf"))
    pq = []
    visited = set()
    heap.heappush(pq,(0,startingNode))
    distance[startingNode] = 0
    parent = defaultdict(lambda : -1)
    
    while pq:
        _,node = heap.heappop(pq)
        visited.add(node)
        
        for nbr,cost in graph[node]:
            if nbr in visited:
                continue
            
            newCost = distance[node] + cost
            if distance[nbr] > newCost:
                distance[nbr] = newCost
                parent[nbr] = node
                heap.heappush(pq,(newCost,nbr))

    return distance,parent


g = {
    0 : [(1,1),(2,4),(3,7)],
    1 : [(0,1),(2,1)],
    2 : [(1,1),(0,4),(3,2)],
    3 : [(0,7),(2,2),(4,3)],
    4 : [(3,3)]
}
print(dijkstra(g,0))