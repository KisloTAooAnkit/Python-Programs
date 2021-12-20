class DSU:
    
    def __init__(self,n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    
    
    def find(self,n1):
        if n1 == self.parent[n1]:
            return n1
        
        p = self.find(self.parent[n1])
        self.parent[n1] = p
        return p
    
    def union(self,n1,n2):
        s1 = self.find(n1)
        s2 = self.find(n2)
        
        if s1 == s2:
            return False
        
        if self.rank[s1] >= self.rank[s2]:
            self.rank[s1] += self.rank[s2]
            self.parent[s2] = s1
            self.rank[s2] = 0
        else:
            self.rank[s2] += self.rank[s1]
            self.parent[s1] = s2
            self.rank[s1] = 0
        return True
    

def kruskal_mst(edges,vertices):
    edges.sort(key = lambda x : x[2])
    dsu = DSU(vertices)
    ans = 0
    for src,dest,cost in edges:
        
        if dsu.union(src,dest):
            ans += cost
    return ans

e = [ [0,1,1] , [1,3,3] , [3,2,4] , [2,0,2] , [0,3,2] , [1,2,2]]
print(kruskal_mst(e,4))