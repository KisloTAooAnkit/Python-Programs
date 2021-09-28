def modifyQueue(q,k):
    # code here
    n = len(q)
    stack = []
    for i in range(0,k):
        stack.append(q.pop(0))
        
    
    while(stack):
        q.append(stack.pop(-1))
        
    
    for i in range(0,n-k):
        val = q.pop(0)
        q.append(val)
    
    return q

q = [1,2,3,4,5]
k = 3
print(modifyQueue(q,k))