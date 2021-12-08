from collections import defaultdict as dict,deque
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
        
    def bfs(self,source,dest=None):
        q = deque()
        visited = dict(bool)
        distance = dict(int)
        parent = dict(int)
        parent[source] = parent
        distance[source] = 0
        visited[source] = True
        q.append(source)
        
        while(q):
            node = q.popleft()
            for vertice in self.adjList[node]:
                if vertice not in visited:
                    visited[vertice] = True
                    parent[vertice] = node
                    distance[vertice] = distance[node] + 1
                    q.append(vertice)
    
        #shortestDistance
        for key in self.adjList:
            print("Shortest Distance from {0} to {1} is {2}".format(source,key,distance[key]))

        #shortest path from source node to dest
        if dest:
            temp = dest
            while(temp != source):
                print(temp,"<-",end=" ")
                temp = parent[temp]
            print(source)

    def __dfsHelper(self,source,visited):
        if source not in visited:
            print(source,end="->")
            visited[source] = True
            for node in self.adjList[source]:
                self.__dfsHelper(node,visited)

    def dfs(self,source):
        print("DFS Traversal from {0}".format(source))
        visited = dict(bool)
        self.__dfsHelper(source,visited)

graph = Graph()
graph.addEdge(0,1)
graph.addEdge(0,4)
graph.addEdge(2,1)
graph.addEdge(3,4)
graph.addEdge(4,5)
graph.addEdge(2,3)
graph.addEdge(3,5)
graph.printAdjList()
graph.bfs(1,5)
graph.dfs(4)