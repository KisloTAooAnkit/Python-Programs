import BuildTreeFromStr
def DFShelper(root,dic,x,y):
    if not root:
        return

    if (x,y) not in dic:
        dic[(x,y)] = [root.data]
    else:
        dic[(x,y)].append(root.data)
    
    DFShelper(root.left,dic,x+1,y-1)
    DFShelper(root.right,dic,x+1,y+1)

def diagonalTraversal(root):
    if not root:
        return []

    ans = []
    dic = dict()
    DFShelper(root,dic,0,0)
    for pair in dic:
        if (pair[0]-1 , pair[1] -1) in dic:
            continue
        else:
            startx = pair[0]
            starty = pair[1]
            while((startx,starty) in dic):
                ans = ans + dic[(startx,starty)]
                startx +=1
                starty +=1
    return ans
    
n = "null"
a = [17 ,29 ,10 ,15 ,28 ,28 ,29 ,4, 4 ,n, n ,n ,n ,n, n ,n ,n ,n ]
root = BuildTreeFromStr.buildTree(a)
print(diagonalTraversal(root))