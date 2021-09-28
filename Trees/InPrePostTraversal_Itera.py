
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
def inPrePostTraversal(node):
    if not node:
        return
    pre = []
    inorder = []
    post = []

    stack = []
    pair = [node,1]
    stack.append(pair)
    while(stack):
        pair = stack[-1]
        if pair[1] == 1:
            pre.append(pair[0].val)
            pair[1] +=1
            if pair[0].left:
                stack.append([pair[0].left,1])
        elif pair[1] == 2:
            inorder.append(pair[0].val)
            pair[1] +=1
            if pair[0].right:
                stack.append([pair[0].right,1])
        else :
            
            post.append(pair[0].val)
            stack.pop(-1)
    print(pre)
    print(inorder)
    print(post)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inPrePostTraversal(root)
            
            
