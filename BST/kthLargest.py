import buildTreeeBST

def inorder(root,k,idx,ans):
    if not root:
        return None
    inorder(root.right,k,idx,ans)
    idx[0] +=1
    if idx[0] == k:
        ans[0] = root.data
        return


    inorder(root.left,k,idx,ans)



def kthLargest(root,k):
    if not root:
        return 
    ans = [-1]
    idx = [0]
    inorder(root,k,idx,ans)
    return ans[0]


arr = [78,69,80,4,72,79]
arr = [9,"null",10]
k = 1
root = buildTreeeBST.buildTree(arr)
print(kthLargest(root,k))