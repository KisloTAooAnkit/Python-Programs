import sys
class Package:
    def __init__(self,minimum=sys.maxsize,maximum=-sys.maxsize,n=0) -> None:
        self.minimum = minimum
        self.maximum = maximum
        self.n = n

def inorder(root,arr):
    if not root:
        return

    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)

def largestBST(root):
    if not root:
        return None
    
    arr =[]
    inorder(root,arr)
    return lenOfLongIncSubArr(arr,len(arr))

def lenOfLongIncSubArr(arr, n) :

    m = 1
    l = 1
      
    # traverse the array from the 2nd element
    for i in range(1, n) :
 
        if (arr[i] > arr[i-1]) :
            l =l + 1
        else :
            if (m < l)  :
                m = l
 
            l = 1
         
         
    
    if (m < l) :
        m = l
      
    
    return m