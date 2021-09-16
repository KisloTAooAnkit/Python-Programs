#https://leetcode.com/problems/merge-two-sorted-lists/submissions/
def merge(head1,head2):
    temp = None
    ansHead = None
    curr1 = head1
    curr2 = head2

    if(head1.data < head2.data):
        temp = head1
        ansHead = head1
        curr1 = curr1.next
    else:
        temp = head2
        ansHead = head2
        curr2 = curr2.next

    while(curr1 and curr2):
        if(curr1.data < curr2.data):
            temp.next = curr1
            curr1 = curr1.next
        else:
            temp.next = curr2
            curr2 = curr2.next

        temp = temp.next

    temp.next = curr1 if curr1 else curr2
    
    return ansHead


a = [[1,6],[1,4]]
a.sort()
print(a)