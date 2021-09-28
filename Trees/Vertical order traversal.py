import sys
def findWidth(node,ans,flag):
    if not node:
        return ans-1
    if flag:
        ans1 = findWidth(node.left,ans+1,flag)
        ans2 = findWidth(node.right,ans-1,flag)
    else:
        ans1 = findWidth(node.left,ans-1,flag)
        ans2 = findWidth(node.right,ans+1,flag)
    return max(ans1,ans2)


def entry(node):
    if not node:
        return None

    leftWidth = findWidth(node,0,True)
    rightWidth = findWidth(node,0,False)
    
    res = [[] for _ in range(leftWidth+rightWidth+1)]
    nodeTraversal(node,leftWidth,res)
    return res


def nodeTraversal(node,idx,res):
    if not node:
        return
    
    res[idx].append(node.val)
    nodeTraversal(node.left,idx-1,res)
    nodeTraversal(node.right,idx+1,res)

"""--------------------------------------------------------------------------------------------------"""
    
def helper(node,dic,x,y):
    if not node:
        return 
    
    if (x,y) in dic:
        dic[(x,y)].append(node.val)
    else:
        dic[(x,y)] = [node.val]
    
    helper(node.left,dic,x+1,y-1)
    helper(node.right,dic,x+1,y+1)

def verticalTraversal(root):
    dic = dict()
    helper(root,dic,0,0)
    leftw = sys.maxsize
    rightw = -sys.maxsize
    for pair in dic.keys():
        dic[pair].sort()
        leftw = min(leftw,pair[1])
        rightw = max(rightw,pair[1])

    ans = [[]]*(-leftw+rightw+1) 
    for pair,arr in sorted(dic.items()):
        idx = pair[1] - leftw
        ans[idx] = ans[idx] +dic[pair]
    return ans

"""---------------------------------------------------------------------------------------------------------------------"""
