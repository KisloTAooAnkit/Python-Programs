from collections import defaultdict as dict,deque
class Graph:
    
    def __init__(self,v) -> None:
        self.adjList = dict(list)
        self.verticeCount = v
               
    def addEdge(self,left,right,isDirected=False):

        self.adjList[left].append(right)
    
    #Find
    def findSuperParent(self,node,parent):
        if parent[node] == -1:
            return node
        
        #return self.findSuperParent(parent[node],parent)
        #path compression
        p = self.findSuperParent(parent[node],parent)
        parent[node] = p
        return p
        
        
    #Union
    def dsu(self,node1,node2,parent,rank):
        parent1 = self.findSuperParent(node1,parent)
        parent2 = self.findSuperParent(node2,parent)
        
        
        if parent1 != parent2: 
            
            if rank[parent1]>=rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
                rank[parent2] = 0
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
                rank[parent1] = 0
                
            return True
        
        else:
            return False
    
    def containsCycle(self):
        #use dsu logic to check if graph contains cycle or not
        parent = [-1]*(self.verticeCount)
        rank = [1]*(self.verticeCount)
        for node in self.adjList:
            for nbr in self.adjList[node]:
                ans = self.dsu(node,nbr,parent,rank)
                if not ans:
                    print("The edge between {0} and {1} is forming cycle".format(node,nbr))
                    return True
        return False

graph = Graph(7)
graph.addEdge(0,1)
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(0,4)
graph.addEdge(5,6)
graph.addEdge(2,5)
graph.addEdge(2,6)
print(graph.containsCycle())