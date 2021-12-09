from collections import defaultdict as dict,deque
class Graph:
    
    def __init__(self) -> None:
        self.adjList = dict(list)
    
    def addEdge(self,left,right):
        self.adjList[left].append(right)
        
    
    def backtrack(self,node,visited,instack):
        
        visited[node] = True
        instack[node] = True
        ans = False
        for nbr in self.adjList[node]:

            if nbr in instack and instack[nbr]:
                return True
            if nbr in visited or nbr not in self.adjList:
                continue
            ans = ans or self.backtrack(nbr,visited,instack)
            
        instack[node] = False
        return ans
    def checkCycle(self):
        visited = dict()
        instack = dict()
        ans = False
        for source in self.adjList:
            if source not in visited:
                ans = ans or self.backtrack(source,visited,instack)
        return ans
    

def canFinish(n,preq):
    g = Graph()
    for src,dest in preq:
        g.addEdge(src,dest)
    return not g.checkCycle()

arr = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

n = 2
print(canFinish(n,arr))