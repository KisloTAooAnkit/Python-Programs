import LL
def RemoveDup(head):
    if(not head.next):
        return head

    dic = dict()
    dic[head.data] = 1
    prev = head
    curr = head.next
    while(curr):
        while(curr and curr.data in dic):

            curr = curr.next
        
        prev.next = curr
        if(not curr):
            break
        dic[curr.data] = 1
        prev = prev.next
        curr=curr.next
    return head



a = [1,1,1,2]
root = LL.arrayToList(a,len(a))
root = RemoveDup(root)
LL.display(root)