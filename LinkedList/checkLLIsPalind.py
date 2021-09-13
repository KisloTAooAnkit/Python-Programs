from LinkedList.reverseLL import reverse
from collections import deque
def isPalindromeHelper(head,queue):
    if(not head):
        return True

    queue.append(head.val)
    ans = isPalindromeHelper(head.next,queue)
    
    if head.val == queue.popleft():
        return ans and True

    return False

#O(n) w/o extra space ... use mid finding approach to get to mid via slow fast pointer
#and as you are travesing the slow pointer at same time take prev pointer and 
# rev list at the same time

def isPalindromOpt(head):
    prev = None
    slow = head
    fast = head
    while(fast and fast.next.next):
        fast = fast.next.next
        tmp = prev
        prev = slow
        slow = slow.next
        prev.next = tmp
    
    #in case of odd length slow middle pe  and fast last mein baitha hoga toh usko 2nd half mein bhejo
    if fast:
        slow = slow.next
    
    while(slow):
        if not slow.data == prev.data:
            return False
        else:
            slow = slow.next 
            prev = prev.next
    return True
            
    
