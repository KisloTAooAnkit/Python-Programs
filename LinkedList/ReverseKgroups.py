import LL
def reverseGroup(head,prevHead,k,i,n):
    prev = prevHead
    curr = head
    print(curr.data,i)
    if(i + k >n):
        return curr
        
    while(curr != None and k>0):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        k-=1
    return prev
    


def reverseK(head,i,k,n):
    if(not head):
        return None
    
    prevHead = reverseK(head.next,i+1,k,n)
    if(i%k==0):
        prevHead = reverseGroup(head,prevHead,k,i,n)
    return prevHead

def getCount(head):
    temp = head # Initialise temp
    count = 0 # Initialise count

    # Loop while end of linked list is not reached
    while (temp):
        count += 1
        temp = temp.next
    return count


def caller(head,k):
    n = getCount(head)
    return reverseK(head,0,k,n)
    

a = [1,2,2,4,5,6,7,8,9,10,11,12]
root = LL.arrayToList(a,len(a))
root = caller(root,4)
LL.display(root)