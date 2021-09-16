def getNthFromLast(head,n):
    start = head
    end = head
    i = 1
    while(i<n):
        end = end.next 
        i+=1
        if not end :
            return None
    
    while(end.next):
        start = start.next
        end = end.next
    
    return start.next