import PrintTree
class Node:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = self.data = val
        self.left = left
        self.right = right

    def makeChild(self,other):
        if self.left == None:
            self.left = other
            return True
        if not self.right :
            self.right = other
            return True
        return False


def treeFromBrackets(string):
    stack = []
  
    n = len(string)
    for i in range(n):
        if string[i] == "(":
            continue
            
        if string[i] == ")":
            if stack:
                stack.pop()
        
        else:
    
            newNode = Node(string[i])
            if stack:
                top = stack[-1]
                top.makeChild(newNode)
            stack.append(newNode)

    return stack[-1]


string = "4(2(3)(1))(6(5))"
root = treeFromBrackets(string)
PrintTree.print2D(root)