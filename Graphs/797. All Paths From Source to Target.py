from collections import defaultdict
def dfs(src,dest,lst,visited,path,ans):
    
    if src == dest:
        path.append(dest)
        ans.append(path[:])
        path.pop()
        return
    
    path.append(src)
    visited[src] = 1
    for nbr in lst[src]:
        if visited[nbr] ==0:
            dfs(nbr,dest,lst,visited,path,ans)
    path.pop()
    visited[src] =0
    return

def allPaths(graph):
    src = 0
    dest = len(graph) -1
    visited = defaultdict(lambda : 0)
    ans = []
    visited
    dfs(src,dest,graph,visited,[],ans)
    return ans
g = [[4,3,1],[3,2,4],[3],[4],[]]

print(allPaths(g))
    