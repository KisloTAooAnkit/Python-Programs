import buildTreeeBST
def findSuccessor(root):
    if not root:
        return -1
    temp = root
    while(temp and temp.left):
        temp = temp.left
    return temp.data

def findPredecessor(root):
    if not root:
        return -1
    temp = root
    while(temp and temp.right):
        temp = temp.right
    
    return temp.data


def findSuccAndPred(root,key,pred,succ):
    if not root:
        return
    if root.data == key:
        newPred,newSucc = findPredecessor(root.left),findSuccessor(root.right)
        pred[0] = pred[0] if newPred == -1 else newPred
        succ[0] = succ[0] if newSucc == -1 else newSucc
        return

    if root.data > key:
        succ[0] = root.data
        return findSuccAndPred(root.left,key,pred,succ)
    else:
        pred[0] = root.data
        return findSuccAndPred(root.right,key,pred,succ)
    
def solution(root,key):
    pred = [-1]
    succ = [-1]
    findSuccAndPred(root,key,pred,succ)
    return (pred[0],succ[0])

arr = [50,30,70,20,40,60,80]
root = buildTreeeBST.buildTree(arr)
print(solution(root,60))