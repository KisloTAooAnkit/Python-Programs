import sys
def inorder(root,low,high):
    if low>high:
        return True
    if not root:
        return False
    
    left = inorder(root.left,low,root.data-1)
    right = inorder(root.right,root.data+1,high)
    return left or right


def isdeadEnd(root):
    if not root:
        return True

    low = 1
    high = sys.maxsize
    return inorder(root,low,high) 
    
