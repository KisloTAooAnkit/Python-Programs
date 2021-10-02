import BuildTreeFromStr
import PrintTree
class Package:
    def __init__(self,node,flag) -> None:
        self.node = node
        self.flag = flag


class Solution:
    
    def findLCA(self,root,p,q):
        if not root:
            return Package(root,False)

        left = self.findLCA(root.left,p,q)
        right = self.findLCA(root.right,p,q)

        if root.val == p or root.val == q:
            return Package(root,True)


        if left.flag and right.flag:
            return Package(root,True)

        if left.flag:
            return left

        if right.flag:
            return right
        return Package(root,False)
    

    
    def lowestCommonAncestor(self, root, p, q):
        ans = self.findLCA(root,p,q)
        return ans.node.val
p =5
q = 4
null = "null"
a = [3,5,1,6,2,0,8,null,7,4]

root = BuildTreeFromStr.buildTree(a)
#PrintTree.print2D(root)
obj = Solution()
print(obj.lowestCommonAncestor(root,p,q))

