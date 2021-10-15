def iterativeInorder(root):
    stack = []
    temp = root
    while(True):

        if temp:
            stack.append(temp)
            temp = temp.left
        
        elif stack:
            print("inorder logic yeha pe aayega")
            current = stack.pop(-1)
            print(current.data)
            current = current.right
        
        else:
            break