class Node:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def FirstNonRepeating(stream):
    ans = ""
    dic = dict()
    start = None
    end = None
    n = len(stream)
    for i in range(n):
        val = stream[i]
        if val not in dic:
            obj = Node(val)
            dic[val] = obj
            if not start:
                start = obj
                end = obj
            else:
                end.next = obj
                obj.prev = end
                end = obj
        elif val in dic:
            
            obj = dic[val]
            if obj:
                if start == end and obj == end:
                    start = None
                    end = None
                elif start == obj:
                    start = obj.next
                elif end == obj:
                    end = obj.prev
                else:
                    obj.prev.next = obj.next
                    obj.next.prev = obj.prev

                dic[val] = None
            
        temp = start
        while(temp):
            print (temp.val,end="")
            temp = temp.next
        print()
        ans +=start.val if start else "#"
    
    return ans

a = "ftvbwnimpvvbfvtot"
print(FirstNonRepeating(a))            



