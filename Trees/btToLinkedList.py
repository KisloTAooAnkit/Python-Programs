#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

import BuildTreeFromStr

class Package:
    def __init__(self,left,right) -> None:
        self.leftNode  : TreeNode = left
        self.rightNode : TreeNode = right 

class TreeNode:
    def __init__(self,data,left=None,right=None) -> None:
        self.data = self.val = data 
        self.left = left 
        self.right = right
        
def returnLLHelper(root: TreeNode)->Package:
    if not root:
        return None

    leftPackage = returnLLHelper(root.left)
    rightPackage = returnLLHelper(root.right)
    
    newNode = root
    newNode.left = None
    ans = Package(newNode,newNode)
    
    if not leftPackage and not rightPackage:
        return ans
    
    if leftPackage:
        newNode.right = leftPackage.leftNode
        if not rightPackage:
            ans.rightNode = leftPackage.rightNode
        
    if rightPackage:
        if leftPackage:
            leftPackage.rightNode.right = rightPackage.leftNode
        else:
            newNode.right = rightPackage.leftNode
        ans.rightNode = rightPackage.rightNode
        
    return ans

    
def returnLL(root):
    ans = returnLLHelper(root)
    temp = ans.leftNode
    while(temp):
        print(temp.data,end=" ")
        temp = temp.right  


arr = [1,2,5,3,4,"null",6]
root = BuildTreeFromStr.buildTree(arr)
returnLL(root)