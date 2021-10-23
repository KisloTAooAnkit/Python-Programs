#https://leetcode.com/problems/maximum-score-from-removing-stones/
import heapq
def maxScore(a,b,c):
    pq = [-a,-b,-c]
    heapq.heapify(pq)
    ans = 0
    while(True):
        val1 = heapq.heappop(pq)
        val2 = heapq.heappop(pq)
        if val1 ==0 or val2 == 0:
            return ans
        val2 += 1
        val1 += 1
        heapq.heappush(pq,val1)
        heapq.heappush(pq,val2)
        ans +=1
    return ans

a = 2
b = 4
c = 6

print(maxScore(a,b,c))