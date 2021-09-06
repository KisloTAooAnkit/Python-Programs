import LL
def addNumber(root):
    if(not root.next):
        if root.data == 9:
            root.data = 0
            return 1 
        else:
            root.data +=1
            return 0
    
    val = addNumber(root.next)
    if root.data == 9:
        root.data = 0
        return 1
    else:
        root.data +=1
        return 0


def addOne(head):
    val = addNumber(head)
    if(val==1):
        newNode = LL.Node(1)
        newNode.next = head
        return head
    else:
        return head
