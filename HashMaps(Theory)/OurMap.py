class MapNode:
    def __init__(self,key,val) -> None:
        self.key = key
        self.value = val
        self.next = None
    

class OurMap:
    
    def __init__(self) -> None:
        self.count = 0 # total kitni entries hai hashmap mein 
        self.numberOfBuckets = 5
        self.bucketArr = [None]*self.numberOfBuckets
        
    
    def __del__(self):
        for idx,_ in enumerate(self.bucketArr):
            del self.bucketArr[idx]
            
    def size(self):
        return self.count
    
    def __getitem__(self,key):
        bucketIdx = self.__getBucketIndex(key)
        head = self.bucketArr[bucketIdx]
        while(head):
            if head.key == key:
                return head.value
        
        
        
        return None
    
    def __setitem__(self,key,value):
        bucketIndex = self.__getBucketIndex(key)
        head = self.bucketArr[bucketIndex]
        while(head):
            if head.key == key:
                head.value = value
                return
            head = head.next
        newNode = MapNode(key,value)
        prevNode = self.bucketArr[bucketIndex]
        newNode.next = prevNode
        self.bucketArr[bucketIndex] = newNode
        self.count +=1
        
        loadFactor = self.numberOfBuckets / self.count
        if loadFactor < 0.7:
            self.__rehash()
        return
        
        
        
    def __delitem__(self,key):
        bucketIdx = self.__getBucketIndex(key)
        head = self.bucketArr[bucketIdx]
        prev = None
        while(head):
            if head.key == key:
                self.count -=1
                if prev:
                    prev.next = head.next
                    del head
                    return
                else:
                    self.bucketArr[bucketIdx] = head.next
                    head.next = None    
                    del head
                    return
            prev = head
            head = head.next
    
    def __getBucketIndex(self,key):
        hashCode = 0
        baseP = 1
        for i in range(len(key)-1,-1,-1):
            hashCode += ord(key[i]) * baseP
            baseP *= 37 #random prime number
            hashCode , baseP = hashCode% self.numberOfBuckets , baseP % self.numberOfBuckets
        return hashCode % self.numberOfBuckets # compression
    
    def __rehash(self):
        temp = self.bucketArr[:]
        self.bucketArr = [None]*(2*self.numberOfBuckets)
        self.numberOfBuckets *=2
        self.count = 0
        for slot in temp:
            head = slot
            if not head:
                continue
            while(head):
                self[head.key] =  head.val
                self.count +=1
                head = head.next
        for slot in temp:
            del slot
        del temp

dic = OurMap()
dic["ankit"] = 1
dic["sumit"] = 2
dic["sumit"] = 4
print(dic["ankit"],dic["sumit"])
