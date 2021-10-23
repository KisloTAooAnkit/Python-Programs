import heapq

class Item:
    def __init__(self,word,freq) -> None:
        self.word = word
        self.freq = freq
    
    def __lt__(self,other):
        if self.freq == other.freq:
            #YEHA PE HAM ULTA RETURN KARHE HAI KYUNKI MIN HEAP SE HAM JAB FINAL ANS POP KARENGE TOH ASC 
            #ORDER MEIN MILEGA AUR USE HAME REVERSE KARNA HOGA(DSC ORDER KE LIYE) IS WAJAH SE CONDITION ULTI HAI
            return self.word > other.word
        return self.freq < other.freq
   
        

            

def topKFreqWords(words,k):
    dic = dict()
    for i in words:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1
    items = [Item(word,freq) for word,freq in dic.items()]
    pq = []
    ans = []
    n = len(items)
    del dic
    for i in range(k):
        pq.append(items[i])
    heapq.heapify(pq)
    for i in range(k,n):
        heapq.heappushpop(pq,items[i])
    
    while pq:
        item = heapq.heappop(pq)
        ans.append(item.word)
    return ans[::-1]


words =["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
print(topKFreqWords(words,k)) 
        
        