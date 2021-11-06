import BuildTreeFromStr
def helper(root,runningNum,totalSum):
    if not root:
        return

    if not root.left and not root.right:
        totalSum[0] += (runningNum*10) + root.data
        return
    
    helper(root.left,runningNum*10 + root.data,totalSum)
    helper(root.right,runningNum*10 + root.data,totalSum)
    return


def sumNum(root):
    ans = [0]
    helper(root,0,ans)
    return ans[0]

arr = [1,2,3]
root = BuildTreeFromStr.buildTree(arr)
print(sumNum(root))