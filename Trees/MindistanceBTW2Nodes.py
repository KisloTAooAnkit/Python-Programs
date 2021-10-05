def helper(root,p,q,flag):
    if not root:
        return -1
    
    left = helper(root.left,p,q,flag)
    right = helper(root.right,p,q,flag)

    ans = -1 if root.val != p and root.val != q else 1
    if flag[0]:
        return max(left,right)

    if left > -1 and right > -1:
        flag[0] = True
        return left + right

    if left> -1 or right > -1:
        if ans>-1:
            flag[0] = True
            return max(left,right)        
        return max(left,right) + 1 

    if left == -1 and right == -1:
        if ans > -1:
            return 1
        return -1
        