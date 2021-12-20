from collections import defaultdict
import heapq
def networkDelay(times,n,k):
    graph = defaultdict(lambda : [])
    for src,des,cost in times:
        graph[src].append((des,cost))
    
    distance = defaultdict(lambda : float("inf"))
    pq = []
    visited = set()
    heapq.heappush(pq,(0,k))
    distance[k] = 0
    while pq:
        _,node = heapq.heappop(pq)
        visited.add(node)
        
        for nbr,cost in graph[node]:
            if nbr in visited:
                continue
            newCost = distance[node] + cost
            if newCost < distance[nbr]:
                distance[nbr] = newCost
                heapq.heappush(pq,(newCost,nbr))
    
    if len(visited) < n:
        return -1
    ans = float("-inf")        
    for _,cost in distance.items():
        ans = max(ans,cost)

        
    return ans
    
    
times = [[1,2,1]]
n = 4
k = 2    
                   
print(networkDelay(times,k))