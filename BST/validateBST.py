#fat gyi onvercomplex solution abana diya tha


import sys
from BST.constructBSTFromPreorder import TreeNode


def inorder(root,prev,first,second):
    if not root:
        return

    inorder(root.left,prev,first,second)
    if not first[0] and prev[0].val > root.val:
        first[0] = prev[0]
    
    if first and prev[0].val > root.val:
        second[0] = root
    
    inorder(root.right,prev,first,second)
    return


def caller(root):
    prev = TreeNode(-sys.maxsize)
    first = [None]
    second = [None]
    inorder(root,prev,first,second)
    first[0].val,second[0].val = second[0].val,first[0].val