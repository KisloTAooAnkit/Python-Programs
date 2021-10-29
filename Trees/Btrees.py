import BuildTreeFromStr
def EdgeTraversal(root):
    flag = False
    leftw = 0
    rightw = 0
    temp = root
    while(temp):
        temp = temp.left
        leftw +=1
    
    temp = root
    while temp:
        if not temp.right and temp.left:
            flag = True
            rightw +=1
            break
        temp = temp.right
        rightw +=1
    
    return (leftw,rightw,flag)
        
def inOrder(root,ans,lh,h,flag):
    if not root:
        return
    if flag[0]:
        return
    if not root.left and not root.right: 
        if h == lh:
            ans[0] +=1
            return
        else:
            flag[0] = True
            return
    inOrder(root.left,ans,lh,h+1,flag)
    inOrder(root.right,ans,lh,h+1,flag)
    return
    

def countNodes(root):
    left,right,flag = EdgeTraversal(root)
    if flag:
        return 2**(left) - 1 -1
    if left == right:
        return 2**(left) -1 
    ans = [0]
    flag = [0]
    inOrder(root,ans,left,1,flag)
    return (2**(left-1) -1) + ans[0]


arr =[1,2,3,4,5,6,7,8,9]
root = BuildTreeFromStr.buildTree(arr)
print(countNodes(root))