from collections import deque
def ZigZagBFS(node):
    if not node :
        return
    ans = []
    flag = False
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
        if flag:
            res = res [::-1]
        flag = not flag
        ans.append(res)
        q.append(None)
        q.popleft()
    return ans


def zigZagTwoStacksApproach(node):
    if not node:
        return 
    curr = [node]
    nxt = []
    ans = []
    flag = True
    while(True):
        while(curr):
            node = curr.pop(-1)
            ans.append(node.val)
            if flag:
                if node.left:
                    nxt.append(node.left)   
                if node.right:
                    nxt.append(node.right)
            else:
                if node.right:
                    nxt.append(node.right)
                if node.left:
                    nxt.append(node.left)
        if not nxt:
            break
        flag = not flag
        curr ,nxt = nxt,[]               
    return ans