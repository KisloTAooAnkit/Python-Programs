from collections import deque,defaultdict
def coinPaths(n,roads):
    graph = defaultdict(list)
    mod = (10**9) + 7
    for src,dest,time in roads:
        graph[src].append([dest,time])
        graph[dest].append([src,time])
    
    q = deque()
    q.append([0,0])
    cost = defaultdict(int)
    
    while q:
        node,time = q.popleft()
        if node == n-1:
            cost[time] +=1
            continue
        for nbr in graph[node]:
            q.append([nbr[0],nbr[1]+time])
    
    ans = float("inf")
    for key in cost:
        ans = min(ans,key)
    print(cost)
    return cost[key]%mod
    

n = 7 
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(coinPaths(n,roads))