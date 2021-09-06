import LL
def findIntersection(head1,head2):
    arr = []
    count = 0
    while(head1 and head2):
        if(head1.data == head2.data):
            arr.append(head1.data)
            count+=1
            head1 = head1.next
            head2 = head2.next
        elif(head1.data<head2.data):
            head1 = head1.next
        else:
            head2 = head2.next
    
    root = LL.arrayToList(arr,count)
    return root
        