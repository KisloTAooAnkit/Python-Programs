def mergeTwoSortedLL(h1,h2):
    t1 = h1
    t2 = h2
    ans = None
    if t1.data < t2.data:
        ans = t1
        head = t1
        t1 = t1.bottom
    else:
        ans = t2
        head = t2
        t2 = t2.bottom
    while(t1 and t2):
        if t1.data < t2.data:
            ans.bottom = t1
            ans = ans.bottom
            t1 = t1.bottom
        else:
            ans.bottom = t2
            ans = ans.bottom
            t2 = t2.bottom
    while(t1):
        ans.bottom = t1
        ans = ans.bottom 
        t1 = t1.bottom
    
    while(t2):
        ans.bottom = t2
        ans = ans.bottom 
        t2 = t2.bottom
    return head
        



def flatten(root):
    
    first = root
    second = root.next
    while(second):
        temp = second
        first = mergeTwoSortedLL(first,temp)
        second = second.next
    return first
        
        
    