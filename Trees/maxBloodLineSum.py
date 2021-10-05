import BuildTreeFromStr
class Package:
    def __init__(self,height,pathSum) -> None:
        self.height = height
        self.pathSum = pathSum
    
class Solution:
    def sumHelper(self,root) -> Package:
        if not root:
            return Package(0,0)
        
        left = self.sumHelper(root.left)
        right = self.sumHelper(root.right)

        if left.height > right.height:
            newSum = left.pathSum + root.val
            newHeight = left.height +1
            return Package(newHeight,newSum)
        
        elif left.height < right.height:
            newSum = right.pathSum + root.val
            newHeight = right.height +1
            return Package(newHeight,newSum)

        #both heights are equal
        return Package(left.height +1 , max(left.pathSum,right.pathSum)+root.val)



    def caller(self,root):
        ans = self.sumHelper(root)
        return ans.pathSum

null = "null"
arr = [1,2,3,4,5,6,7]
root = BuildTreeFromStr.buildTree(arr)
ob = Solution()
print(ob.caller(root))