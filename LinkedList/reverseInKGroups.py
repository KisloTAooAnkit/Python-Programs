def actualRev():
    pass


def reverseList(head,k) :
    prev = None
    curr = head
    end = head
    while(k and curr):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        k-=1
    start = prev
    return [start,end]
        


def reverseInK(head,k):
    temp = head
    i =0
    while(temp):
        if(i%k != 0):
            temp=temp.next
        start,end = reverseList(temp,k-1)
