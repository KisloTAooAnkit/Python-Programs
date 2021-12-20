
def findSuperParent(n,parent):
    if parent[n] == n:
        return n
    p = findSuperParent(parent[n],parent)
    return p

def union(node1,node2,parent,rank):
    s1 = findSuperParent(node1,parent)
    s2 = findSuperParent(node2,parent)
    
    if s1 != s2:
        if rank[s1] > rank[s2]:
            rank[s1] += rank[s2]
            rank[s2] = 0
            parent[s2] = s1
        else:
            rank[s2] += rank[s1]
            rank[s1] = 0
            parent[s1] = s2
        return True
    else:
        return False
    


def sol(edges):
    n = len(edges)
    parent = [i for i in range(n+1)] 
    rank = [1]*(n+1)
    
    for src,dest in edges:
        ans = union(src,dest,parent,rank)
        if not ans:
            return[src,dest]   