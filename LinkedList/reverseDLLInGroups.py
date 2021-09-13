def reverseBlock(head,k):
    start = head
    end = head
    while(end.next and k>0):
        end= end.next
        k-=1
    last = end
    while(last != start and start.prev != last):
        start.data,last.data = last.data,start.data
        start= start.next
        last = last.prev
    
    return end.next



def reverseDLLInGroups(head,k):
    
    curr = head
    while(curr):
        curr = reverseBlock(curr,k-1)
    
    return head
