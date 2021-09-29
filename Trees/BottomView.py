import BuildTreeFromStr
class Item:

    def __init__(self,node,x,y) -> None:
        self.node = node
        self.x = x
        self.y = y
    def __lt__(self,other):
        if self.y == other.y:
            return self.x < other.x
        return False
    

def DFS(node,dic,x,y):
    if not node:
        return
    currI = Item(node,x,y)
    if y in dic:
        if dic[y].x == currI.x:
            dic[y] = currI
        else:
            dic[y] = currI  if dic[y] < currI else dic[y]
    else:
        dic[y]= currI

    DFS(node.left,dic,x+1,y-1)
    DFS(node.right,dic,x+1,y+1)
    return 

def bottomView(node):
    if not node:
        return []
    dic = dict()
    DFS(node,dic,0,0)
    leftw = float('inf')
    rightw = - float('inf')
    for key in dic:
        leftw = min(leftw,key)
        rightw = max(rightw,key)
    ans = [0]*(-leftw+rightw +1)
    it = sorted(dic.keys())
    for key in it:
        ans[key-leftw] = dic[key].node.val
    return ans

null = "null"



tree = [1,2,3,10,9,4,5,null,null,null,null,null,null,6,null,7,null,8]
tree = [14 ,14 ,3 ,null ,8 ,8, 12, null ,6 ,17, 3, null, 1 ,11 ,10 ,null ,6 ,6 ,13, null ,10 ,17, 7, null ,11 ,7]
root = BuildTreeFromStr.buildTree(tree)

print(bottomView(root))
