
from collections import defaultdict
import heapq as heap

def cheapestFlightWithingKStops(n,flights,src,dst,k):
    graph = defaultdict(lambda : [])
    
    for s,d,c in flights:
        graph[s].append((d,c))
    
    distance = defaultdict(lambda : defaultdict(lambda : float("inf")))
    pq = []
    visited = set()
    ans = float("inf")
    distance[src][k+1] = 0
    heap.heappush(pq,(0,src,k+1))
    
    while(pq):
        
        _,node,steps = heap.heappop(pq)
        
        visited.add(node)
        
        if steps <= 0 and node != dst:
            continue
        
        if node == dst:
            ans = min(ans,distance[node][steps])
            continue
        for nbr,cost in graph[node]:
            if nbr in visited:  
                pass
            newCost = distance[node][steps] + cost
            newStep = steps -1
            if distance[nbr][newStep] > newCost:
                distance[nbr][newStep] = newCost
                heap.heappush(pq,(newCost,nbr,newStep))
    
    return ans 
            


n = 3
flights =[[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
src = 0
dst = 2
k = 4

print(cheapestFlightWithingKStops(n,flights,src,dst,k))