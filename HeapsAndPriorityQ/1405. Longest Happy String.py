import heapq
from collections import deque
def longestHappyString(a,b,c):

    pq = []

    for idx,val in enumerate([a,b,c]):
        char = "a"
        if val>0:
            if idx == 1:
                char = "b"
            if idx == 2:
                char = "c"
            pq.append((-val,(char,0)))
            
                


    heapq.heapify(pq)
    ans = []
    cooldownQ = deque()
    qlen = 0
    while pq:

        count,pair = heapq.heappop(pq)
        letter,cd = pair
        ans.append(letter)
        count +=1
        cd +=1
        if qlen>0:    
            qlen-=1
            heapq.heappush(pq,cooldownQ.popleft())
        if count < 0:
            if cd == 2:
                
                cooldownQ.append((count,(letter,0)))
                qlen+=1
            else:
                heapq.heappush(pq,(count,(letter,cd)))


    return "".join(ans)

a= 7
b=1
c=0
print(longestHappyString(a,b,c))