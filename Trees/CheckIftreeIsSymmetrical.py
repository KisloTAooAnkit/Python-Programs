class Solution:
    
    def helper(self,root1,root2):
        if not root1 and not root2:
            return True
        elif not root1 and root2 or not root2 and root1:
            return False
        
        val1 = self.helper(root1.left,root2.right)
        val2 = self.helper(root1.right,root2.left)
        return val1 and val2 and (root1.val == root2.val)
        
    
    def isSymmetric(self, root) -> bool:
        return self.helper(root.left,root.right)
    