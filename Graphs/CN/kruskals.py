# def changeParent(node,destParent,parent):
#     if parent[node] == node:
#         parent[node] = destParent
#         return
#     changeParent(parent[node],destParent,parent)



class Edge:
    def __init__(self,src,dest,cost) -> None:
        self.src = src
        self.dest = dest
        self.cost = cost    
    
    def __lt__(self,other):
        return self.cost < other.cost
    
def getParent(node,parent):
    if parent[node] == node:
        return node
    getParent(parent[node],parent)

def kruskals(inpEdges,totalVertices):
    parent = [0]*totalVertices
    for i in range(totalVertices):
        parent[i] = i
    mstEdges  = []
    inpEdges.sort()
    count = 0
    i = 0
    while(count < (totalVertices-1)):
        edge : Edge = inpEdges[i]
        srcParent = getParent(edge.src,parent)
        destParent = getParent(edge.dest,parent)
        i+=1
        if srcParent == destParent:
            continue
        parent[destParent] = srcParent
        mstEdges.append(edge)
        count +=1
        
    return mstEdges
    

def takeInput():
    pass
    verticesCount,edgesCount = list(map(int,input("Enter no. of vertices & edges : ").strip().split()))
    inputEdges = []
    for i in range(edgesCount):
        source,dest,weight = list(map(int,input("Source Dest Weight : ").strip().split()))
        inputEdges.append(Edge(source,dest,weight))

    mstEdges = kruskals(inputEdges,verticesCount)
    for edge in mstEdges:
        if edge.src < edge.dest:
            print(edge.src, "to",edge.dest,"cost",edge.cost)
        else:
            print(edge.dest, "to",edge.src,"cost",edge.cost)
takeInput()