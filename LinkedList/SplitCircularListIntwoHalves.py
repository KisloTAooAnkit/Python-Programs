def breakChain(head):
    temp = head.next
    prev = head
    start = head
    while(start!=temp):
        prev = temp
        temp = temp.next
    prev.next = None
    return start

def findMid(head):
    slow = head
    fast = head
    while(fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    return slow.next

def splitList(head):
    if(not head.next):
        return head , None
    head1 = breakChain(head)
    head2 = findMid(head)
    return head1 , head2