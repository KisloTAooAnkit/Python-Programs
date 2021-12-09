from collections import defaultdict as dict,deque
class Graph:
    
    def __init__(self) -> None:
        self.adjList = dict(list)
    
    def addEdge(self,left,right):
        self.adjList[left].append(right)

    def checkCycle(self,node,visited,instack):

        
        visited[node] = True
        instack[node] = True
        ans = False        
        #do recursion on edges
        for newNode in self.adjList[node]:
            if newNode in instack and instack[newNode]:
                return True
            
            if newNode in visited or newNode not in self.adjList:
                continue
            ans = ans or self.checkCycle(newNode,visited,instack)
            #early return kyunki we have to just find if there is a cycle once 
            if ans:
                return True
        #pop/undo
        instack[node] = False
        return ans
    
    def hasCycle(self) -> bool:
        visited = dict(bool)
        instack = dict(bool)
        ans = False
        for node in self.adjList:
            if node not in visited:
                ans = ans or self.checkCycle(node,visited,instack)
        return ans      

graph = Graph()
graph.addEdge(0,1)
graph.addEdge(0,4)
graph.addEdge(0,5)
graph.addEdge(5,4)
#graph.addEdge(1,2)
#graph.addEdge(2,3)
#graph.addEdge(3,1)
print(graph.adjList)
print(graph.hasCycle())
