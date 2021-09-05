import LL
def deleteDuplicates(head):

    curr = head
    while(fwd):
        fwd = curr
        while(fwd and fwd.data == curr.data):
            fwd=fwd.next
        
        curr.next = fwd
        curr = curr.next
    return head