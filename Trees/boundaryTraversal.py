import BuildTreeFromStr
import PrintTree
def isLeaf(node):
    if node.left == None and node.right == None:
        return True
    return False


def leftBoundary(root,ans):
    stack = [root]
    while stack:
        node = stack.pop()
        if node and not isLeaf(node):
            ans.append(node.data)
            if node.left:
                stack.append(node.left)
            elif node.right:
                stack.append(node.right)

def getLeaves(root,ans):
    if not root:
        return
    if isLeaf(root):
        ans.append(root.data)
    
    getLeaves(root.left,ans)
    getLeaves(root.right,ans)
    return


def rightBoundary(root,ans):
    temp = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node and  not isLeaf(node):
            temp.append(node.data)
            if node.right:
                stack.append(node.right)
            elif node.left:
                stack.append(node.left)
    for node in temp[::-1]:
        ans.append(node)


def printBoundary(root):
    ans = [root.data]
    leftBoundary(root.left,ans)
    getLeaves(root,ans)
    rightBoundary(root.right,ans)
    return ans


N = "null"
null = "null"
arr = [1,2,null,3,null,4,null,5,null]
#arr = [4, 10, N ,5 ,5 ,N ,6 ,7 ,N ,8 ,8 ,N ,8 ,11, N ,3 ,4 ,N ,1 ,3 ,N ,8 ,6 ,N ,11, 11, N, 5 ,8]
arr = [20, 8 ,22, 4 ,12, N, 25 ,N ,N, 10 ,14]
root = BuildTreeFromStr.buildTree(arr)
#PrintTree.print2D(root)
print(printBoundary(root))
