def toSumTree(root):
    if not root:
        return 0

    left = toSumTree(root.left)
    right = toSumTree(root.right)
    currentVal = root.data
    root.data = left + right
    return root.data + currentVal