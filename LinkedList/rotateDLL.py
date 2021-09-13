def rotateDLL(head,k):
    temp = head

    while(temp.next):
        temp = temp.next
    
    temp.next = head
    head.prev = temp

    cur = head
 
    while(k>0):
        cur = cur.next
        k-=1
    

    prev = cur.prev
    cur.prev = None
    prev.next = None

    return cur
