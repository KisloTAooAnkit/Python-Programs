class Node:
    def __init__(self,val,left=None,right=None) -> None:
        self.data = val
        self.left = left
        self.right = right

def helper(arr,start,end):
    if start>end:
        return None
    
    mid = start + (end-start)//2
    rootVal = arr[mid]
    leftChild = helper(arr,start,mid-1)
    rightChild = helper(arr,mid+1,end)
    return Node(rootVal,leftChild,rightChild)