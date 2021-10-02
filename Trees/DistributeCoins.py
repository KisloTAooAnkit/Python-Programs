def distCoins(root,ans):
    if not root:
        return 0
    
    left = distCoins(root.left,ans)
    right = distCoins(root.right,ans)
    ans[0] += (abs(left) + abs(right))
    return left + right -1 + root.val
    