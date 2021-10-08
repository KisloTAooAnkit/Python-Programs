import BuildTreeFromStr
class Package:
    def __init__(self,valid,nodeSum) -> None:
        self.isValid = valid
        self.nodeSum = nodeSum

def sumTreeHelp(root)->Package:
    if not root:
        return Package(True,0)
    
    if not root.left and not root.right:
        return Package(True,root.data)
    
    left = sumTreeHelp(root.left)
    right = sumTreeHelp(root.right)

    valid = left.isValid and right.isValid
    ansSum = left.nodeSum + right.nodeSum

    if valid and root.data == ansSum:
        return Package(True,root.data+ansSum)
        
    return Package(False,nodeSum=root.data)

def sumTree(root):
    ans = sumTreeHelp(root)
    return ans.isValid


n = N = null = "null"
arr = [62 ,16 ,15, null ,8 ,4, 7, null ,8, 4]

root = BuildTreeFromStr.buildTree(arr)
print(sumTree(root))
