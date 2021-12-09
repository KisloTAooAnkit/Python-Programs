from collections import defaultdict as dict,deque
class Graph:
    
    def __init__(self) -> None:
        self.adjList = dict(list)
    
    def addEdge(self,left,right,isDirected=False):
        if not isDirected:
            self.adjList[left].append(right)
            self.adjList[right].append(left)
            
    def __hasCycle(self,node,visited,parent):
        if node in visited:
            return True
        
        ans = False
        visited[node] = True
        for newNode in self.adjList[node]:
            if newNode == parent:
                continue
            ans = ans or self.__hasCycle(newNode,visited,node)
        return ans
    
    def hasCycle(self) -> bool:
        visited = dict(bool)
        ans = False
        for node in self.adjList:
            if node not in visited:
                ans = ans or self.__hasCycle(node,visited,node)
        return ans

graph = Graph()
graph.addEdge(0,1)
graph.addEdge(0,4)
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(4,5)
graph.addEdge(4,3)
graph.addEdge(5,3)
print(graph.hasCycle())
