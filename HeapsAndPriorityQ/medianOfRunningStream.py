import heapq

class MedianFinder:

    def __init__(self):
        self.leftSide = []
        self.rightSide = []
        heapq.heapify(self.leftSide)
        heapq.heapify(self.rightSide)
        self.leftLen = 0
        self.rightLen = 0
        self.flag = 0    
        

    def addNum(self, num: int) -> None:

        #leftSide insertion
        if self.flag == 0:

            #check on rightSide
            if self.rightLen != 0 and self.rightSide[0] < num:
                val = heapq.heappushpop(self.rightSide,num)  
                heapq.heappush(self.leftSide,-val)
            else:
                heapq.heappush(self.leftSide,-num)
            self.leftLen +=1
        
        #rightSide insertion
        else:
            #check on leftside
            if -self.leftSide[0] >= num:
                val = -heapq.heappushpop(self.leftSide,-num)
                heapq.heappush(self.rightSide,val)
            else:
                heapq.heappush(self.rightSide,num)
            self.rightLen +=1
        
        self.flag = 1 - self.flag
        

            

    def findMedian(self) -> float:
        if self.leftLen == self.rightLen:
            return (-self.leftSide[0] + self.rightSide[0])//2
        else:
            return -self.leftSide[0]


obj = MedianFinder()

obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())