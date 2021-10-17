class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.qsize ==  0 

    def getSize(self):
        return len(self.pq)
    
    def getMin(self):
        if not self.isEmpty:
            return self.pq[0]
        else:
            return 0
    
    def insertMin(self,data):
        self.pq.append(data)
        childIdx = self.getSize() - 1
        while(childIdx>0):
            parentIdx = (childIdx - 1) // 2
            if self.pq[childIdx] < self.pq[parentIdx]:     
                self.pq[childIdx],self.pq[parentIdx] = self.pq[parentIdx],self.pq[childIdx]
            else:
                break
            childIdx = parentIdx        
    
    def peekQueue(self):
        print(self.pq)
    
    def popMin(self):

        ans = self.getMin()
        self.pq[0] = self.pq.pop(-1)
        n = self.getSize()
        parentIdx = 0
        child1 = 2*(parentIdx) +1 
        child2 = 2*(parentIdx) +2
        while(child1 < n):
            minIdx = parentIdx
            if self.pq[minIdx]>self.pq[child1] :
                minIdx = child1
            if child2<n and  self.pq[minIdx] > self.pq[child2]:
                minIdx = child2
            
            self.pq[minIdx],self.pq[parentIdx] = self.pq[parentIdx],self.pq[minIdx]
            parentIdx = minIdx
            child1 = 2*parentIdx +1 
            child2 = 2*parentIdx +2
            
        return ans

objPQ = PriorityQueue()

objPQ.insertMin(12)
objPQ.insertMin(6)
objPQ.insertMin(5)
objPQ.insertMin(100)
objPQ.insertMin(1)
objPQ.insertMin(9)
objPQ.insertMin(0)
objPQ.insertMin(14)
objPQ.peekQueue()
print(objPQ.popMin())
objPQ.peekQueue()