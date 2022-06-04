import random
class RandomizedCollection:

    def __init__(self):
        self.dic = dict()
        self.arr = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.dic:
            #increase count
            self.dic[val][1] +=1
            return False
        
        self.arr.append(val)
        self.length +=1
        self.dic[val] = [self.length-1,1]
        return True    

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        idx,count = self.dic[val]
        
        if count > 1:
            self.dic[val][1] -=1
            return True
        
        lastElement = self.arr.pop()
        del self.dic[val]
        self.length -=1
        
        if lastElement == val:
            return True

        else:
            self.arr[idx] = lastElement
            self.dic[lastElement][0] = idx
            return True

    def getRandom(self) -> int:
        return random.choice(self.arr)