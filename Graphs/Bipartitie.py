

from collections import defaultdict, deque



def check(edges):
    
    graph = defaultdict(lambda : [])
    
    for src,dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)

    
    redSet,blueSet = set(),set()
    flag = True #true = redset insertion , #false = blue set insert
    q = deque()
    redSet.add(0)
    q.append(0)
    while(q):
        for _ in range(len(q)):
            val = q.popleft()
            if flag:
                redSet.add(val)
            else:
                blueSet.add(val)
            for nbr in graph[val]:
                if flag:
                    if nbr in redSet:
                        return False
                    else:
                        if not nbr in blueSet:
                            blueSet.add(nbr)
                            q.append(nbr)
                else:
                    if nbr in blueSet:
                        return False
                    else:
                        if not nbr in redSet:    
                            redSet.add(nbr)
                            q.append(nbr)
        flag = not flag
    return True                            

edges = [[0,1],[1,2],[2,3],[3,4],[0,4]]
print(check(edges=edges))