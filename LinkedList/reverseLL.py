def reverse(prev,curr):
    if(not curr):
        return prev

    temp = curr.next
    curr.next = prev
    return reverse(curr,temp)

def reverseList(head) :
    prev = None
    curr = head
    while(curr):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
        