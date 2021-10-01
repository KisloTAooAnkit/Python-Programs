from collections import deque

class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.data = val


def buildTree(s):

    if len(s) == 0  or s[0] == "null":
        return None
    ip = s

    root = Node(int(ip[0]))
    size = 0
    
    q = deque()
    q.append(root)
    size +=1

    i =1

    while(size>0 and i < len(ip)):
        currNode = q.popleft()
        size -=1

        currVal = ip[i]

        if (currVal != "null"):
            currNode.left = Node(int(currVal))

            q.append(currNode.left)
            size+=1
        i+=1
        if(i>=len(ip)):
            break
        currVal = ip[i]

        if currVal != "null":
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size = size+1
        i+=1
    return root

    