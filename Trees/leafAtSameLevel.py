import BuildTreeFromStr

def checkH(root,ans):
    if not root:
        return 0
    
    leftH = checkH(root.left,ans)
    rightH = checkH(root.right,ans)

    if leftH == 0 and rightH != 0:
        return rightH + 1
    if rightH ==0 and leftH != 0:
        return leftH +1
    
    if leftH != rightH:
        ans[0] = False
    return max(leftH,rightH) +1
    



def caller(root):
    ans = [True]
    checkH(root,ans)
    return ans[0]

null = "null"

arr =[1691 ,6733 ,null ,5989 ,6640, null ,2750 ,3565, null, 1371 ,5003 ,null ,1677, 8921, null ,8413 ,7729 ,null ,7679 ,2475 ,null ,2822 ,6415, null ,3872]
 
#arr = [10,20,30,10,1,null,2,null,4,2,null,5,null,null,null,null,3,null,5]

root = BuildTreeFromStr.buildTree(arr)

print(caller(root))