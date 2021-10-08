class Node:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = self.data = val
        self.left = left
        self.right = right


def treeCreatorHelper(inarr,prearr,inStart,inEnd,preStart,preEnd,hashmap):
    if inStart>inEnd:
        return None
    
    rootData = prearr[preStart]
    rootIdx = hashmap[rootData]
    # for i in range(inStart,inEnd+1):
    #     if inarr[i] == rootData:
    #         rootIdx = i
    #         break
    
    L_inStart = inStart
    L_inEnd = rootIdx -1
    L_preStart = preStart + 1
    L_preEnd = L_inEnd - L_inStart + L_preStart
    R_inStart = rootIdx +1
    R_inEnd = inEnd
    R_preStart = L_preEnd + 1
    R_prEnd = preEnd
        
    leftChild = treeCreatorHelper(inarr,prearr,L_inStart,L_inEnd,L_preStart,L_preEnd,hashmap)
    rightChild = treeCreatorHelper(inarr,prearr,R_inStart,R_inEnd,R_preStart,R_prEnd,hashmap)
    
    newNode = Node(rootData)
    newNode.left = leftChild
    newNode.right = rightChild
    
    return newNode

def buildTree(inorder,preorder):
    hashmap = dict()
    for idx,key in enumerate(inorder):
        hashmap[key] = idx
    root = treeCreatorHelper(inorder,preorder,0,len(inorder)-1,0,len(preorder)-1,hashmap)
    return root

