def helper(root,mx):
    if not root:
        return -1
    
    left = helper(root.left,mx)
    right = helper(root.right,mx)

    maxval = root.val
    minVal = root.val

    if left !=-1:
        mx[0] = max(mx[0],abs(root.val-left[0]))
        mx[0] = max(mx[0],abs(root.val-left[1]))
        maxval = max(maxval,left[0],left[1])
        minVal = min(minVal,left[0],left[1])
    
    if right != -1:
        mx[0] = max(mx[0],abs(root.val-right[0]))
        mx[0] = max(mx[0],abs(root.val-right[1]))
        maxval = max(maxval,right[0],right[1])
        minVal = min(minVal,right[0],right[1])
    
    return (minVal,maxval)


def sol(root):
    ans = [0]
    helper(root,ans)
    return ans[0]