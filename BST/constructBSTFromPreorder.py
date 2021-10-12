import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def insertNode(root,value):
    if not root:
        newNode = TreeNode(value)
        return newNode

    if value <root.val:
        root.left = insertNode(root.left,value)
    else:
        root.right = insertNode(root.right,value)
    
    return root


def constructOpt(arr,n,idx,low,high):
    if low>high or idx[0] >=n or arr[idx[0]] <low or arr[idx[0]] >high:
        return None
    
    newNode = TreeNode(arr[idx[0]])
    idx[0] +=1
    if(idx[0]<n and arr[idx[0]]<newNode.val):
        newNode.left = constructOpt(arr,n,idx,low,newNode.val-1)

    elif(idx[0]<n and arr[idx[0]]>newNode.val):
        newNode.right = constructOpt(arr,n,idx,newNode.val +1,high)
    
    return newNode


def construct(arr):
    n = len(arr)
    if n<1:
        return 
    idx = [0]
    root = constructOpt(arr,n,idx,-sys.maxsize,sys.maxsize)
    return root

arr = [8,5,1,7,10,12]
construct(arr)