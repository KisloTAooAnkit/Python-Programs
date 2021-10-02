import BuildTreeFromStr
class Helper:
    def __init__(self,ans,h) -> None:
        self.ans = ans
        self.h = h

def checkBalancedHelper(root):
    if not root:
        return Helper(True,0)
    
    left = checkBalancedHelper(root.left)
    right = checkBalancedHelper(root.right)
    currh = max(left.h,right.h) +1
    if (left.ans and right.ans) and (abs(left.h - right.h) <= 1):
        return Helper(True,currh)
    else:
        return Helper(False,0)

def isBalanced(root):
    res = checkBalancedHelper(root)
    return res.ans

null = "null"
arr = [3,9,20,null,null,15,7]
root = BuildTreeFromStr.buildTree(arr)
print(isBalanced(root))
