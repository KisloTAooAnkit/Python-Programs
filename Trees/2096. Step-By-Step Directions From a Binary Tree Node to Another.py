def findLCASpaceOpt(root,p,q):
    if not root:
        return None
    left = findLCASpaceOpt(root.left,p,q)
    right = findLCASpaceOpt(root.right,p,q)
    
    if left and right:
        return root
    if root.data == q or root.data == p:
        return root
    if left:
        return left
    if right:
        return right
    return None


def genPath(root,val,arr):
    if not root:
        return False
    if root.val == val:
        return True
    arr.append("L")
    ans = genPath(root.left,val,arr)
    if ans:
        return True
    arr.pop()
    arr.append("R")
    ans = genPath(root.right,val,arr)
    if ans:
        return True
    arr.pop()   
    return False


def sol(start,end,root):
    lca =findLCASpaceOpt(root,start,end)
    ans = []
    genPath(lca,start,ans)
    for i,val in enumerate(ans):
        ans[i] = "U"
    genPath(lca,end,ans)
    return ans    