import BuildTreeFromStr
import sys

def helper(root,ans):
    if not root:
        return -sys.maxsize
    left = helper(root.left,ans)
    right = helper(root.right,ans)

    arcSum = left + right + root.val
    leftarcSum = left+root.val
    rightarcSum = right + root.val
    ans[0] = max(arcSum,ans[0],root.val,leftarcSum,rightarcSum)
    return max(leftarcSum,rightarcSum,root.val)


def maxPathSum(self) -> int:
    ans = [-sys.maxsize]
    x = self.helper(root,ans)
    return max(ans[0],x)
        
null = "null"
ans=[-sys.maxsize]
arr = [-1,null,9,-6,3,null,null,null,-2]
root = BuildTreeFromStr.buildTree(arr)
print(helper(root,ans),ans[0])