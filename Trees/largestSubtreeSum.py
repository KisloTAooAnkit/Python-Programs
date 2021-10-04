def largestSum(root,ans):
    if not root:
        return 0


    left = largestSum(root.left,ans)
    right = largestSum(root.right , ans)
    currentSum = root.val + left + right

    ans[0] = max(currentSum,ans[0])

    return currentSum