import BuildTreeFromStr
from collections import deque


def printBoundary(root):
    ans = []
    q = deque()
    q.append(root)
    q.append(None)
    while(len(q)>1):
        val = q.pop()

N = "null"
null = "null"
arr = [1,2,2,3,3,null,null,4,4]
root = BuildTreeFromStr.buildTree(arr)
print(printBoundary(root))
