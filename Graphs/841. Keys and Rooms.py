from collections import defaultdict,deque
def keysAndRooms(rooms):
    
    totalRooms = len(rooms)
    q = deque()
    q.append(0)
    visited = defaultdict(bool)
    visited[0] = True
    while q:
        val = q.popleft()
        totalRooms -=1
        for key in rooms[val]:
            if visited[key] == True:
               continue
            visited[key] = True
            q.append(key)
    
    return totalRooms == 0

r =  [[1,3],[3,0,1],[2],[0]]
print(keysAndRooms(r)) 
    