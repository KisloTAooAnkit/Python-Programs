



class Node:
    def __init__(self,key,val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    

class DLinkedList:
    def __init__(self) -> None:
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    

    def addFront(self,node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
    
    def deleteLast(self):
        temp = self.tail.prev
        self.tail = self.tail.prev
        return temp

    def deleteNode(self,node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def refreshNode(self,node):
        self.deleteNode(node)
        self.addFront(node)
    
class LRUCache:
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.currentSize = 0
        self.hashmap = dict()
        self.DLL = DLinkedList()
    
    def get(self,key):
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.DLL.refreshNode(node)
        return node.val

    def put(self,key,val):

        if self.capacity == 0:
            return 

        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = val
            self.DLL.refreshNode(node)
            return
        if self.currentSize == self.capacity:
            node = self.DLL.deleteLast()
            del self.hashmap[node.key] 
            del node
            self.currentSize -=1

        self.currentSize +=1
        node = Node(key,val)
        self.hashmap[key] = node
        self.DLL.addFront(node)