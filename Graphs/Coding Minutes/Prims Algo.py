from collections import defaultdict,deque
import heapq
class Graph:
    
    def __init__(self):
        self.adjList = defaultdict(list)
        
        
    def addEdge(self,s,d,w):
        self.adjList[s].append((d,w))
        self.adjList[d].append((s,w))
        
    def prims_mst(self):
        pq = []
        visited = defaultdict(bool,lambda : False)
        ans = 0
        
        #begin
        heapq.heappush(pq,(0,0)) #weight node
        while pq:
            weight,dest = heapq.heappop(pq)
            if visited[dest]:
                continue
            ans += weight
            visited[dest] = True
            
            for nbr,wght in self.adjList[dest]:
                if not visited[nbr]:
                    heapq.heappush((wght,nbr)) 
        return ans