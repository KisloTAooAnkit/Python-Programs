def helper(root,succ):
    if not root:
        return None
    
    if not root.left and not root.right:
        root.next = succ
        return root

    left = helper(root.left,root)
    right = helper(root.right,succ)

    if right:
        root.next = right
    else:
        root.next = succ
    return root if not left else left 
