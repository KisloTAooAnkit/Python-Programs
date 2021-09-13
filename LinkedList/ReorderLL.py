#https://leetcode.com/problems/reorder-list/
def reorderLL(head):
    slow = head
    fast = head
    n = linkedListLen(head)
    while(fast.next and fast):
        slow = slow.next
        fast = fast.next.next
    
    revHead = reverseLL(slow)
    count = n//2 if n%2 != 0 else (n//2) -1 
    ptr1 = head
    ptr2 = revHead
    while(count>0):

        temp1 = ptr1.next
        temp2 = ptr2.next

        ptr1.next = ptr2
        ptr2.next = temp1
        ptr1 = temp1
        ptr2 = temp2

        count-=1
    
    return head






def reverseLL(head):
    prev = None
    curr = head
    while(curr):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def linkedListLen(head):
    count  =0
    while(head):
        count+=1
        head=head.next
    return count