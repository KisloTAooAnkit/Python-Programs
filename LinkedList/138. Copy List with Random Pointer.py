class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    randomMap = dict()
    nodeMap = dict()
    prev = None
    temp = head
    head2 = None
    while(temp):
        node = Node(temp.val)
        
        if prev:
            prev.next = node
        if not prev:
            head2 = node
        prev = node
        randomMap[temp] = temp.random
        nodeMap[temp] = node
        temp = temp.next
    
    temp1 = head
    temp2 = head2
    while(temp1):
        randomNode = None
        if randomMap[temp1]:
            randomNode = nodeMap[temp1.random]
        temp2.random = randomNode
        temp1 = temp1.next
        temp2 = temp2.next
    return head2
    



