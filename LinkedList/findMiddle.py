def middNode(head):
    prev = None

    slow = head
    fast = head
    while(fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    

    return slow

import LL
a = [1,2,3,4,5,7]
root = LL.arrayToList(a,len(a))
print(middNode(root).data)