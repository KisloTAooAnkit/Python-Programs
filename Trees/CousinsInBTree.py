from collections import deque
import BuildTreeFromStr
class Package:
    def __init__(self,parent=None,h=0) -> None:
        self.parent = parent
        self.h = h

def isCousins(root,x,y):
    q = deque()
    q.append((root,None,0))
    if root.val == x or root.val == y:
        return False
    ans  = []
    while(q):
        
        if len(ans) == 2:
            break

        node,parent,depth = q.popleft()

        if node.val == x or node.val == y:
            ans.append(Package(parent,depth))

        if node.left:
            q.append((node.left,node,depth+1)
        
        if node.right:
            q.append((node.right,node,depth+1)
    
    x , y = ans

    return x.parent != y.parent and x.h == y.h 

arr = [1,2,3,4,5,6]
x = 4
y = 6
root = BuildTreeFromStr.buildTree(arr)
print(isCousins(root,x,y))