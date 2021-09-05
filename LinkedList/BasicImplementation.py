class Node :
    val = None
    next = None
    def __init__(self,val,next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    head = None
    def __init__(self,headNode) -> None:
        self.head = headNode

    def printLL(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next



n1 = Node(4)
n2 = Node(3,n1)
n3 = Node(5,n2)
n4 = Node(6,n3)
LL = LinkedList(n4)
LL.printLL()
