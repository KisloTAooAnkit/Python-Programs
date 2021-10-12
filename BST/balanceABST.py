

def inOrder(root,arr):
    if not root:
        return None
    
    inOrder(root.left)
    arr.append(root)
    inOrder(root.right)


def balanceTheBST(arr,start,end):
    if start>end:
        return None
    
    mid = start + (end-start)//2
    Lstart = start
    Lend = mid-1
    Rstart = mid+1
    Rend = end
    leftChild = balanceTheBST(arr,Lstart,Lend)
    rightChild = balanceTheBST(arr,Rstart,Rend)
    node = arr[mid]
    node.left = leftChild
    node.right = rightChild
    return node




def balanceBST(root):
    arr = []
    inOrder(root)
    root = balanceTheBST(arr,0,len(arr)-1)
    return root
