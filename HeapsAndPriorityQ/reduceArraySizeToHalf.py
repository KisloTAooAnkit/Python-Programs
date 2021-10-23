import heapq
def minSetSize(arr):
    dic = dict()
    for i in arr:
        dic[i] = dic.get(i,0) +1
    
    pq = [(-value,key) for key,value in dic.items()]
    del dic
    heapq.heapify(pq)
    n = len(arr)
    c = n//2
    ans = 0
    while(n > c):
        freq,key = heapq.heappop(pq)
        n = n + freq
        ans +=1
    return ans