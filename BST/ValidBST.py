from Trees import BuildTreeFromStr
import sys
class Package:
    def __init__(self,isBst,maxVal = -sys.maxsize, minVal = sys.maxsize) -> None:
        self.isBst = isBst
        self.maxVal = maxVal
        self.minVal = minVal
        

def isValidBSTHelperBtUp(root)->Package:
    if not root:
        return Package(True)
    
    left = isValidBSTHelperBtUp(root.left)
    right = isValidBSTHelperBtUp(root.right)
    
    if not left.isBst or not right.isBst:
        return Package(False)
    isBst = left.maxVal < root.val and right.minVal > root.val
    maxVal = max(left.maxVal,root.val,right.maxVal)
    minVal = min(right.minVal,root.val,left.minVal) 
    return Package(isBst,maxVal,minVal)

def isValidBSTHelperTpDwn(root,low,high):
    if not root:
        return True
    if low > root.val or root.val > high:
        return False
    
    left = isValidBSTHelperTpDwn(root.left,low,root.val-1)
    right = isValidBSTHelperTpDwn(root.right,root.val+1,high)
    return left and right 
        
    

def isValidBST(root):
    ans = isValidBSTHelperBtUp(root)
    return ans.isBst

n = "null"
arr = [2,1,5,0,10,6,8]
root = BuildTreeFromStr.buildTree(arr)
print(isValidBST(root))

