from collections import defaultdict as dict
class Graph:
    
    def __init__(self) -> None:
        self.adjList = dict(list)
    
    
    def addEdge(self,left,right,isDirected=False):
        if not isDirected:
            self.adjList[left].append(right)
            self.adjList[right].append(left)
        else:
            self.adjList[left].append(right)
    
    def printAdjList(self):
        for key,val in self.adjList.items():
            print(key,":",val)


graph = Graph()
graph.addEdge(0,1)
graph.addEdge(0,4)
graph.addEdge(2,1)
graph.addEdge(3,4)
graph.addEdge(4,5)
graph.addEdge(2,3)
graph.addEdge(3,5)
graph.printAdjList()