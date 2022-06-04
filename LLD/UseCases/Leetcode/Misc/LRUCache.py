

class DLLNode:

    def __init__(self,key,val,prev=None,nxt=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt


class LRUCache:
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.cacheSize = 0
        self.head = None
        self.tail = None
        self.hash = dict()


    def get(self,key):
        if key not in self.hash:
            print(-1)
            return -1
        self.put(key,self.hash[key].val)
        print(self.hash[key].val)
        return self.hash[key].val

    def put(self,key,val):
        if key in self.hash:
            self.remove(node=self.hash[key])
        
        newNode = DLLNode(key,val)
        self.hash[key] = newNode
        
        self.add(newNode)

        if self.cacheSize > self.capacity:
            self.remove(self.tail)

        


    
    def add(self,node):
        if self.cacheSize ==0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.cacheSize +=1
        return



    def remove(self,node):
        if self.cacheSize ==0 :
            return 
        prev = node.prev
        nxt = node.next
        if prev:
             prev.next = nxt
        if nxt:
            nxt.prev = prev
        if node == self.tail:
            self.tail = node.prev
        if node == self.head:
            self.head = node.next
        self.cacheSize -=1
        del self.hash[node.key]
        return


if __name__ == "__main__":
        
    lRUCache = LRUCache(2);
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    lRUCache.get(1)
    lRUCache.put(3,3)
    lRUCache.get(2)
    lRUCache.put(4,4)
    lRUCache.get(1)
    lRUCache.get(3)
    lRUCache.get(4)
