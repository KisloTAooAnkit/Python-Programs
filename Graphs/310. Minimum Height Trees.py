from collections import defaultdict,deque
class Graph:

    def __init__(self) -> None:
        self.adjList = defaultdict(list)

    
    def addEdge(self,src,dest):
        self.adjList[src].append(dest)
        self.adjList[dest].append(src)
    

    def smallestPath(self,source):
        q = deque()
        ans = 0
        q.append(source)
        visited = dict()
        visited[source] = 1
        n = 1
        while n:
            for i in range(n):
                val = q.popleft()
                n-=1
                for nbr in self.adjList[val]:
                    if nbr not in visited:
                        q.append(nbr)
                        visited[nbr] = 1
                        n+=1
            ans +=1
        return ans



def minHTrees(n,edges):
    graph = Graph()
    for src,dest in edges:
        graph.addEdge(src,dest)
    ans = []
    minLen = float("inf")
    for src in range(n):
        res = graph.smallestPath(src)
        if res < minLen:
            ans.clear()
            ans.append(src)
            minLen = res
        elif res == minLen:
            ans.append(src)
    return ans


edges = [[1,0],[1,2],[1,3]]
print(minHTrees(4,edges))