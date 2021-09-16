def mergeTwoSortedLL(head1,head2):
    if not head1:
        return head2
    if not head2:
        return head1
    
    temp = None
    resHead = None
    curr1 = head1
    curr2 = head2
    if(head1.data<head2.data):
        temp = head1
        resHead = head1
        curr1 = curr1.bottom
    else:
        temp = head2
        resHead = head2
        curr2 = curr2.bottom
    
    while(curr1 and curr2):
        if curr1.data < curr2.data:
            temp.bottom = curr1
            curr1 = curr1.bottom
        else:
            temp.bottom = curr2
            curr2 = curr2.bottom
        temp = temp.bottom
    
    if curr1:
        temp.bottom = curr1
    elif curr2:
        temp.bottom = curr2
    
    return resHead

def flatten(head):
    prev = None
    curr = head
    
    while(curr):
        prev = mergeTwoSortedLL(prev,curr)
        curr = curr.next
        prev.next = None
    return prev
