def findStartOfLoop(head):
    if not head and not head.next:
        return None

    slow = head
    fast = head
    while(fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            while(slow !=fast):
                fast = fast.next
                slow = slow.next
            return slow
    
    return None


