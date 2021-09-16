#by changing links
import LL 
def sort012(head):
    firstZero = None
    firstTwo = None
    firstOne = None
    lastOne = None
    lastZero = None
    lastTwo = None

    curr =head
    while(curr):
        if curr.data == 1 and firstOne == None:
            firstOne = curr
            lastOne = curr
        elif curr.data == 0 and firstZero == None:
            firstZero = curr
            lastZero = curr
        
        elif curr.data == 2 and firstTwo == None:
            firstTwo = curr
            lastTwo = curr
        curr = curr.next


    curr = head
    while(curr):
        val = curr.data
        if val == 0 and curr != lastZero:
            lastZero.next = curr
            lastZero = curr
        elif val == 1 and curr != lastOne:
            lastOne.next = curr
            lastOne = curr
        elif val == 2 and curr != lastTwo:
            lastTwo.next = curr
            lastTwo = curr
        curr = curr.next
    if lastTwo:
        lastTwo.next = None

    if  firstZero:
        if not firstOne:
            lastZero.next = firstTwo
        else:
            lastZero.next = firstOne
            lastOne.next = firstTwo
        return firstZero
    
    if firstOne:
        lastOne.next = firstTwo
        return firstOne

    if firstTwo:
        return firstTwo

a = [2,2,0,1]
n = len(a)
root = LL.arrayToList(a,n)
root = sort012(root)
LL.display(root)
