def isIsomorphic(root1,root2):
    if not root1 and not root2:
        return True
    if  not root1 or not root2:
        return False
    
    if root1.data != root2.data:
        return False
    
    
    return (isIsomorphic(root1.left,root2.left) and (isIsomorphic(root1.right,root2.right)) 
            or 
            (isIsomorphic(root1.left,root2.right) and (isIsomorphic(root1.right,root2.left))))