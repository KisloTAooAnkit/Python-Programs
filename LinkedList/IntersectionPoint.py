
def getCount(head):
    temp = head
    count = 0
    while(temp):
        count+=1
        temp = temp.next
    return count

def helper(head1,head2,extraNodes):
    while(extraNodes):
        head1 = head1.next
        extraNodes -=1
    while(head1 != head2):
        head1= head1.next
        head2 = head2.next
    return head1

    

def getIntersectionNode(head1,head2):
    c1 = getCount(head1)
    c2 = getCount(head2)
    if(c1>c2):
        return helper(head1,head2,abs(c1-c2))
    else:
        return helper(head2,head1,abs(c1-c2))
