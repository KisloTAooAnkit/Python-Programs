def inorder(root,arr):
    if not root:
        return
    
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)


def preorder(root,arr,idx,n):
    if not root or idx[0]>=n:
        return
    
    root.data = arr[idx[0]]
    idx[0] +=1
    print(root.data)
    preorder(root.left,arr,idx,n)
    preorder(root.right,arr,idx,n)
    return


def convertBST(root):
    arr = []
    idx = [0]
    inorder(root,arr)
    n = len(arr)
    preorder(root,arr,idx,n)

