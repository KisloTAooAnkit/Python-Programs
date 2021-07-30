#https://leetcode.com/problems/maximum-binary-tree/

import sys
class TreeNode:
    val =0
    left = None
    right = None
    
    def __init__(self,val =0,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(arr):
    n = len(arr)
    if(n==0):
        return None
    idx =-1
    maxval = -sys.maxsize
    for i in range(n):
        if(arr[i]>maxval):
            idx = i
            maxval = arr[i]
    
    Root = TreeNode(maxval)
    Root.left = constructMaximumBinaryTree(arr[:idx])
    Root.right = constructMaximumBinaryTree(arr[idx+1:])
    return Root
        