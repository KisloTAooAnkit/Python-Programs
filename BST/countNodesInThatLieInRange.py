import buildTreeeBST

def inorder(root,low,high,ans):
    if not root:
        return 
    
    inorder(root.left,low,high,ans)
    if low<=root.data<=high:
        ans[0] +=1
    inorder(root.right,low,high,ans)

def getCount(root,low,high):
    ans = [0]
    inorder(root,low,high,ans)
    return ans[0]

n = "null"
root = buildTreeeBST.buildTree([10,5,50,1,n,40,100])
L = 5
R= 45
print(getCount(root,L,R))