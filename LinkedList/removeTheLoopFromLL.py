def solveLoopInLL(head):
    slow = head
    fast = head
    prev = head
    
    if not head and not head.next:
        return head
    
    while(fast.next and fast.next.next):
        prev = slow
        slow = slow.next
        fast = fast.next
    
        if slow == fast:
            slow = head
            while(slow != fast):
                prev = slow 
                slow = slow.next
                fast = fast.next
            prev.next = None
            return head
    
    return head