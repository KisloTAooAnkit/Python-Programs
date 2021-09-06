#https://leetcode.com/problems/add-two-numbers/ 
#NOTE:numbers here are stored in Reverse Order

from LinkedList.BasicImplementation import Node


def getCount(head):
    temp = head
    count = 0
    while(temp):
        count+=1
        temp = temp.next
    return count
def addTwoNumbersHelper(head1,head2):
    prev =0
    past = None
    while(head1 and head2):
        
        val = head1.data + head2.data + prev
        head1.data = val%10
        prev  = 1 if val > 9 else 0
        head1 = head1.next
        head2 = head2.next
    while(head1):
        val = head1.data + prev
        head1.data = val%10
        prev  = 1 if val > 9 else 0
        past = head1
        head1 = head1.next

    if prev == 1:
       root = Node(1)
       past.next = root

def addTwoNumbers(head1,head2):
    c1 = getCount(head1)
    c2 = getCount(head2)
    if(c1>c2):
        addTwoNumbersHelper(head1,head2)
        return head1
    else:
        addTwoNumbersHelper(head2,head1)
        return head2


