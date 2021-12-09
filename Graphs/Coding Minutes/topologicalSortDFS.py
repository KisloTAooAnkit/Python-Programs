from collections import defaultdict as dict,deque
class Graph:
    
    def __init__(self) -> None:
        self.adjList = dict(list)
    
    def addEdge(self,left,right):
        self.adjList[left].append(right)
    
    
    def __dfs(self,node,visited,ordering : deque):
        visited[node] = True
        #because node 5 dosent have any entry in adj list but that self.adjList[node] will
        #give error on line 26 as out dict got changed in between
        if node in self.adjList:
            for neighbours in self.adjList[node]:
                if neighbours not in visited:
                    self.__dfs(neighbours,visited,ordering)
        ordering.appendleft(node)
    
    def topologicalSort(self):
        visited = dict()
        ordering = deque()
        
        #we call dfs from every node if it is not visited
        for node in self.adjList:
            if node not in visited:
                self.__dfs(node,visited,ordering)
        
        while ordering:
            print(ordering.popleft(),end=" ")


graph = Graph()
graph.addEdge(0,2)
graph.addEdge(2,3)
graph.addEdge(3,5)
graph.addEdge(4,5)
graph.addEdge(1,4)
graph.addEdge(1,2)
graph.topologicalSort()