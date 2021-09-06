def middNode(head):
    slow = head
    fast = head
    while(fast.next and fast):
        slow = slow.next
        fast = fast.next.next
    return slow