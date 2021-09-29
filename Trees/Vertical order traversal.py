import sys
def findWidth(node,ans,flag):
    if not node:
        return ans-1
    if flag:
        ans1 = findWidth(node.left,ans+1,flag)
        ans2 = findWidth(node.right,ans-1,flag)
    else:
        ans1 = findWidth(node.left,ans-1,flag)
        ans2 = findWidth(node.right,ans+1,flag)
    return max(ans1,ans2)


def entry(node):
    if not node:
        return None

    leftWidth = findWidth(node,0,True)
    rightWidth = findWidth(node,0,False)
    
    res = [[] for _ in range(leftWidth+rightWidth+1)]
    nodeTraversal(node,leftWidth,res)
    return res


def nodeTraversal(node,idx,res):
    if not node:
        return
    
    res[idx].append(node.val)
    nodeTraversal(node.left,idx-1,res)
    nodeTraversal(node.right,idx+1,res)

"""--------------------------------------------------------------------------------------------------"""
    
def helper(node,dic,x,y):
    if not node:
        return 
    
    if (x,y) in dic:
        dic[(x,y)].append(node.val)
    else:
        dic[(x,y)] = [node.val]
    
    helper(node.left,dic,x+1,y-1)
    helper(node.right,dic,x+1,y+1)

def verticalTraversal(root):
    dic = dict()
    helper(root,dic,0,0)
    leftw = sys.maxsize
    rightw = -sys.maxsize
    for pair in dic.keys():
        dic[pair].sort()
        leftw = min(leftw,pair[1])
        rightw = max(rightw,pair[1])

    ans = [[]]*(-leftw+rightw+1) 
    for pair in dic:
        idx = pair[1] - leftw
        ans[idx] = ans[idx] +dic[pair]
    return ans  

"""---------------------------------------------------------------------------------------------------------------------"""
from collections import deque
class QueueItem:
    def __init__(self,node,x,y) -> None:
        self.node = node
        self.x = x
        self.y = y
    def __lt__(self,other):
        return self.node.val < other.node.val

def BFS(node):
    item = QueueItem(node,0,0)
    dic = dict()
    q = deque(item)
    while(q):
        item = q.popleft()
        pair = (item.x,item.y)
        if pair in dic:
            dic[pair].append(item.node.val)
        else:
            dic[pair] = item.node.val

        if item.node.left:
            x = pair[0] + 1
            y = pair[1] - 1
            q.append(QueueItem(item.node.left,x,y))

        if item.node.right:
            x = pair[0] + 1
            y = pair[1] + 1
            q.append(QueueItem(item.node.left,x,y))
    
    leftw = sys.maxsize
    rightw = -sys.maxsize
    for key in dic:
        dic[key].sort()
        leftw = min(key[1],leftw)

        rightw = max(key[1],rightw)
    
    res = [[] for _ in range(leftw+rightw+1)]
    for key in dic:
        idx = key[1] - leftw
        res[idx] = res[idx] + dic[key]
    
    return res

    


