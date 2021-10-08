class Node:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = self.data = val
        self.left = left
        self.right = right

def treeCreatorHelper(postOrder,inOrder,inStart,inEnd,postStart,postEnd,hashmap):
    if inStart>inEnd:
        return None
    
    rootData = postOrder[postEnd]
    rootIdx = hashmap[rootData]
    
    L_inStart = inStart
    L_inEnd = rootIdx-1
    R_inStart = rootIdx +1
    R_inEnd = inEnd

    L_postStart = postStart 
    L_postEnd =  (L_inEnd - L_inStart) + L_postStart
    R_postStart = L_postEnd + 1
    R_postEnd = postEnd -1
    
    leftChild = treeCreatorHelper(postOrder,inOrder,L_inStart,L_inEnd,L_postStart,L_postEnd,hashmap)
    rightChild = treeCreatorHelper(postOrder,inOrder,R_inStart,R_inEnd,R_postStart,R_postEnd,hashmap)
    
    newNode = Node(rootData)
    newNode.left = leftChild
    newNode.right = rightChild
    return newNode


def buildTree(inorder,postorder):
    hashmap = dict()
    for idx,key in enumerate(inorder):
        hashmap[key] = idx
    root = treeCreatorHelper(postorder,inorder,0,len(inorder)-1,0,len(postorder)-1,hashmap)
    return root

