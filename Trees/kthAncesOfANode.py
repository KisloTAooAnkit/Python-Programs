class Package:
    def __init__(self,node=None,height=-1) -> None:
        self.node=node
        self.height=height  


def kthAncestorHelper(root,k,val) -> Package:
    if not root:
        return None

    left = kthAncestorHelper(root.left,k)
    right = kthAncestorHelper(root.right,k)

    pckg = left if not right else right
    h = -1 if not pckg else pckg.height 

    if root.data == val:
        return Package(root,1)

    if h==k:
        return Package(root,h+1)

    if h >-1:
        return Package(pckg.node,h+1)
    
    return None



