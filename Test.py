
def dfsHelper(root):
    if not root:
        return (0,0)

    left = dfsHelper(root.left)
    right = dfsHelper(root.right)

    rootInc = root.val + left[1] + right[1]
    rootNotInc = max(left) + max(right)
    return (rootInc,rootNotInc)

def maxIndependetSet(root):
    dfsHelper(root)