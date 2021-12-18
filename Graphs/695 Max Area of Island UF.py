def findSuperParent(node,parent):
    if node == parent[node]:
        return node
    
    p = findSuperParent(parent[node],parent)
    parent[node] = p
    return p


def doUnion(node1,node2,rank,parent):
    s1 = findSuperParent(node1,parent)
    s2 = findSuperParent(node2,parent)

    if s1 != s2:
        if rank[s1]>=rank[s2]:
            parent[s2] = s1
            rank[s1] += rank[s2]
            rank[s2] = 0
        else:
            parent[s1] = s2
            rank[s2] += rank[s1]
            rank[s1] = 0



def maxAreaIsland(grid):
    directions = [[0,1],[1,0],[0,-1],[-1,0]]

    rows = len(grid)
    cols = len(grid[0])

    rank = []
    for i in range(rows):
        for j in range(cols):
            rank.append(grid[i][j])
    parent = [i for i in range(rows*cols)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                continue
            for dx,dy in directions:
                destX = i + dx
                destY = j + dy
                if destX >= rows or destX < 0 or destY >= cols or destY < 0 or grid[destX][destY] == 0:
                    continue
                node1 = i*cols + j
                node2 = destX*cols + destY
                doUnion(node1,node2,rank,parent)
    return max(rank)


grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

print(maxAreaIsland(grid))