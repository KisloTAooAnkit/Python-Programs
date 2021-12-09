from collections import defaultdict as dict,deque
class Graph:
    
    def __init__(self) -> None:
        self.adjList = dict(list)
    
    def addEdge(self,left,right):
        self.adjList[left].append(right)
    
    
    def topologicalSort(self):
        indegree = dict(int)
        
        #indegree
        for node in self.adjList:
            for neighbours in self.adjList[node]:
                indegree[neighbours] +=1

        #main logic
        q = deque()
        for node in self.adjList:
            if node not in indegree:
                indegree[node] = 0
                q.append(node)
        
        #process the nodes
        while q:
            node = q.popleft()
            print(node,end=" ")
            for neighbours in self.adjList[node]:
                indegree[neighbours] -=1
                if indegree[neighbours] == 0:
                    q.append(neighbours)

graph = Graph()
graph.addEdge(0,2)
graph.addEdge(2,3)
graph.addEdge(3,5)
graph.addEdge(4,5)
graph.addEdge(1,4)
graph.addEdge(1,2)
graph.topologicalSort()