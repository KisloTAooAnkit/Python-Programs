


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.ans = []
        self.combinationLen = combinationLength
        self.generatePerm("",characters,0)
        self.currentPermIdx = 0
        self.permLen = len(self.ans)
        
    
    
    
    def generatePerm(self,word,chars,count):
        if count == self.combinationLen:
            self.ans.append(word)
        
        for i in range(len(chars)):
            self.generatePerm(word+chars[i],chars[i+1:],count+1)
        return
    
    
    def next(self) -> str:
        val = self.ans[self.currentPermIdx]
        self.currentPermIdx +=1
        return val

    def hasNext(self) -> bool:
        return self.currentPermIdx < self.permLen
    

obj = CombinationIterator("abc",2)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())