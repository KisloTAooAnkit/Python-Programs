import Trees.BuildTreeFromStr
def helper(ans,root):
    if not root:
        return 0

    left = helper(ans,root.left)
    right = helper(ans,root.right)

    arcsum = root.val + left + right
    leftarcsum = root.val + left
    rightarcSum = root.val + right
    ans[0] = max(ans[0],arcsum,leftarcsum,rightarcSum,root.val)
    return max(leftarcsum,rightarcSum,root.val)



def maxPath(root):
    ans = [-1001]
    res = helper(ans,root)
    ans[0] = max(ans[0],res)
    return ans


arr = [1,2,3]
root = Trees.BuildTreeFromStr.buildTree(arr)
print(maxPath(root))