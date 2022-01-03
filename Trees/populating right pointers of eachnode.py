from collections import deque
def solve(root):
    

    q = deque()
    q.append(root)
    n = 1
    while(q):
        prev = None
        for i in range(n):
            node = q.popleft()
            n-=1
            if prev:
                prev.next = node
            if node.left:
                n+=1
                q.append(node.left)
            if node.right:
                n+=1
                q.append(node.right)
            prev = node
    return root


def solveOpt(node):

    if not node:
        return 

    prev = None
    curr = node
    while(curr):
        if prev:
            prev.right.next = curr.left
        curr.left.next = curr.right
        prev = curr
        curr = curr.next

    
    solveOpt(node.left)
    solveOpt(node.right)

