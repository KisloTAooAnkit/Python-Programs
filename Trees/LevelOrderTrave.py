from collections import deque
def levelOrderTravBFS(node):
    if not node :
        return
    ans = []
    q = deque()
    q.append(node)
    q.append(None)
    while(q):
        res = []
        while(q[0]):
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not res:
            break
        ans.append(res)
        q.append(None)
        q.popleft()
    return ans


def DFS(node,level,res):
    if not node :
        return
    #har level mein shurat ke time ek khaali dabba us level ke elements ko store karne ke liye
    if level == len(res):
        res.append([])
    
    '''Preorder traversal har level pe left child apni jagah fix karlenge uss level ki subarray ke liye''' 
    res[level].append(node.val)
    DFS(node.left,level+1,res)
    DFS(node.right,level+1,res)


def levelOrderDFS(node):
    res = []
    DFS(node,0,res)
    return res
            


    