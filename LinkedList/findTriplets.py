import ArrToDLL
def findTriplets(head,k):
    curr = head
    end = head
    ans = 0
    while(end.next):
        end = end.next
    
    while(curr.next.next.next):
        start = curr.next
        last = end
        while(start!=None and last!= None and start != last):
            val = curr.data + start.data+ last.data
            if(val>k):
                last = last.prev
            elif(val<k):
                start = start.next
            else:
                ans+=1
                start = start.next
        curr = curr.next
    return ans

arr = [1,2,4,5,6,8,9]
k = 17
start = None
start = ArrToDLL.createList(arr,len(arr),start)
print(findTriplets(start,k))