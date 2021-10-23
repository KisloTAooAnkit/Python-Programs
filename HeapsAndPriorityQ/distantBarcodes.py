import heapq
def rearrBarcodes(barcodes):
    dic = dict()
    for i in barcodes:
        dic[i] = dic.get(i,0) +1
    
    pq = [(-freq,key) for key,freq in dic.items()]
    heapq.heapify(pq)
    prev_freq,prev_key = 0,0
    ans = []
    while(pq):
        freq,key = heapq.heappop(pq)
        ans.append(key)
        freq +=1
        if prev_freq < 0:
            heapq.heappush(pq,(prev_freq,prev_key))
        
        prev_key = key
        prev_freq = freq
    return ans
barcodes = [1,1,1,1,2,2,3,3]
print(rearrBarcodes(barcodes)) 