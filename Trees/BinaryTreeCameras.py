import BuildTreeFromStr
import PrintTree

#-----------------------------------------------------------------------------------

class Status:
    def __init__(self,camera:bool,obsv:bool) -> None:
        self.camera = camera
        self.obsv = obsv

#-----------------------------------------------------------------------------------


def minCameraHelper(root,ans):
    if not root:
        return Status(False,True)
    
    left = minCameraHelper(root.left,ans)
    right = minCameraHelper(root.right,ans)
    
    if not (left.obsv and right.obsv):
        root.val = 1
        ans [0] +=1
        return Status(True,True)
    
    if left.obsv and right.obsv and (not left.camera and not right.camera):
        return Status(False,False)
    
    if (left.camera or right.camera) and (left.obsv and right.obsv) :
        return Status(False,True)
#-----------------------------------------------------------------------------------
def minCameraHelperOpt(self,root,ans):
    if not root:
        return 2

    left = self.minCameraHelper(root.left,ans)
    right = self.minCameraHelper(root.right,ans)

    if left == 1 or right == 1:
        root.val = 1
        ans [0] +=1
        return 3

    if left == 2 and right == 2:
        return 1

    if left ==3 or right == 3 and (left>1 and right >1) :
        return 2

#-----------------------------------------------------------------------------------

    
def minCamera(root):
    ans = [0]
    finalStatus = minCameraHelper(root,ans)
    if finalStatus.obsv:
        return ans[0]
    else:
        return ans[0] +1

null = "null"
arr = [0,0,null,0,null,0,null,null,0]
root = BuildTreeFromStr.buildTree(arr)
print("ans",minCamera(root))
PrintTree.print2D(root)
