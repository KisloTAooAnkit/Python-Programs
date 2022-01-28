import heapq
class Item:
    
    def __init__(self,price,x,y,d) -> None:
        self.x = x
        self.y = y
        self.d = d 
        self.price = price
        
    
    def __gt__(self,other):
        
        if self.d != other.d:
            return self.d < other.d
        elif self.price != other.price:
            return self.price < other.price
        elif self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y
    
    
    
def dfs(visited,grid,x,y,n,m,k,pq,d,pricing):
    if x>=n or x<0 or y>=n or y<0:
        return
    if visited[x][y] or grid[x][y] == 0:
        return 
    visited[x][y] = True
    if pricing[0] <= grid[x][y] <= pricing[1]:
        if len(pq) == k:
            heapq.heappushpop(pq,Item(grid[x][y],x,y,d))
        else:
            heapq.heappush(pq,Item(grid[x][y],x,y,d))

    dfs(visited,grid,x+1,y,n,m,k,pq,d+1,pricing)
    dfs(visited,grid,x,y+1,n,m,k,pq,d+1,pricing)
    dfs(visited,grid,x-1,y,n,m,k,pq,d+1,pricing)
    dfs(visited,grid,x,y-1,n,m,k,pq,d+1,pricing)
    return

def solve(grid,pricing,start,k):
    n = len(grid)
    m = len(grid[0])
    v = [[False]*m for _ in range(n)]
    pq = []
    dfs(v,grid,start[0],start[1],n,m,k,pq,0,pricing)
    
    ans = []
    while(pq):
        val = heapq.heappop(pq)
        ans.append([val.x,val.y])
    ans.sort()
    return ans


grid = [[1,2,0,1],
        [1,3,0,1],
        [0,2,5,1]]
pricing = [2,5]
start = [0,0]
k = 3
print(solve(grid,pricing,start,k))