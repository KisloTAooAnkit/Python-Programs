import buildTreeeBST
def LCAHelper(root,n1,n2,oneFound,twoFound):
    if not root:
        return
    
    ans1 = None
    ans2 = None

    if not oneFound[0]:
        if root.val == n1:
            ans1 = root
            oneFound[0] = True
        elif(n1<root.val):
            ans1 = LCAHelper(root.left,n1,n2,oneFound,twoFound)
        else:
            ans1 = LCAHelper(root.right,n1,n2,oneFound,twoFound)
    if not twoFound[0]:
        if root.val == n2:
            ans2 = root
            twoFound[0] = True
        elif(n2<root.val):
            ans2 = LCAHelper(root.left,n1,n2,oneFound,twoFound)
        else:
            ans2 = LCAHelper(root.right,n1,n2,oneFound,twoFound)
    

    if (ans1 and ans2):
        return root
    if ans1:
        return ans1
    if ans2:
        return ans2

    return None

def LCAOptimized(root,n1,n2):
    while(True):
        if(root.val < n1 and root.val <n2):
            root = root.right
        elif(root.val>n1 and root.val > n2):
            root = root.left
        else:
            return root


def LCA(root,n1,n2):
    n1F = [False]
    n2F = [False]
    return LCAOptimized(root,n1,n2)

n= "null"
arr = [5,4,6,3,n,n,7]
n1 = 4
n2 = 3
root = buildTreeeBST.buildTree(arr)
print(LCA(root,n1,n2).data)
