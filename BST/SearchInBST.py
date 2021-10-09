
def searchBST(root,data):
    if not root:
        return None
    
    if root.data == data:
        return root
    
    ans = None
    if root.data > data:
        ans = searchBST(root.left,data)
    else:
        ans = searchBST(root.right,data)
    return ans

def searchBSTIter(root,data):
    while root and root.val != data:
        root = root.left if root.val > data else root.right
    return root