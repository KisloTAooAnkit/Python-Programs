import buildTreeeBST
def inorder(root,dic):
    if not root:
        return
    inorder(root.left,dic)
    dic[root.val] = 1
    inorder(root.right,dic)

def countPairsOpt(root1,root2,x):
    ans = 0
    temp1 = root1
    temp2 = root2
    stack1 =[]
    stack2 =[]

    while True:
        if temp1 or temp2:
            if temp1:
                stack1.append(temp1)
                temp1 = temp1.left
            if temp2:
                stack2.append(temp2)
                temp2 = temp2.right
        
        elif stack1 and stack2:
            leftp = stack1[-1]
            rightp = stack2[-1]
            
            if leftp.data + rightp.data == x:
                ans+=1
                print(leftp.data,rightp.data)
                node1 = stack1.pop()
                node2 = stack2.pop()
                temp1 = node1.right
                temp2 = node2.left
            elif leftp.data + rightp.data < x:
                temp1 = stack1.pop()
                temp1 = temp1.right
            else:
                temp2 = stack2.pop()
                temp2 = temp2.left
        else:
            break
    return ans




def countPairs(root1,root2,x):
    dic1 = dict()
    dic2 = dict() 
    inorder(root1,dic1)
    inorder(root2,dic2)
    ans = 0
    for key in dic1:
        if x-key in dic2:
            ans+=1
    return ans
n = "null"
root1 = buildTreeeBST.buildTree([1,"null",3,2])
root2 = buildTreeeBST.buildTree([3,2,4,1])
x = 4
print(countPairsOpt(root1,root2,x))