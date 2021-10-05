def pruneTreeHelper(root):
    if not root:
        return 0

    left = pruneTreeHelper(root.left)
    right = pruneTreeHelper(root.right)

    if left == 0 :
        root.left = None
        
    if right == 0:
        root.right = None
        
    if left == 1 or right == 1:
        return 1
    
    return root.val


    