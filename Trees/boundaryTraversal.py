import BuildTreeFromStr
def RightDFS(root,ans,level):
    if not root:
        return
    if level == len(ans):
        ans.append(root.data)
    RightDFS(root.right,ans,level+1)
    RightDFS(root.left,ans,level+1)


def DFS(root,ans,level):
    if not root.left and not root.right:
        ans.append(root.data)
        return
    if len(ans) == level:
        ans.append(root.data)
    
    if root.left:
        DFS(root.left,ans,level+1)
    if root.right:
        DFS(root.right,ans,level+1)
    return

def printBoundary(root):
    ans = []
    DFS(root,ans,0)
    ans.pop(-1)
    newAns = []
    print("before",ans)
    RightDFS(root,newAns,0)
    print("after",newAns)
    newAns = newAns[::-1]
    newAns.pop()
    return ans + newAns

N = "null"
null = "null"
arr = [1,2,2,3,3,null,null,4,4]
root = BuildTreeFromStr.buildTree(arr)
print(printBoundary(root))
