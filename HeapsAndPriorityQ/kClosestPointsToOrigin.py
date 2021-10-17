import math
import heapq
def distance(pair):
    a = pair[0]**2
    b = pair[1]**2
    return math.sqrt(a+b)

def kClosest(points,k):
    pq = []
    n = len(points)
    for i in range(k):
        entry = (-distance(points[i]),points[i])
        pq.append(entry)
    heapq.heapify(pq)
    for i in range(k,n):
        newEntry = (-distance(points[i]),points[i])
        heapq.heappush(pq,newEntry)
        heapq.heappop(pq)
    ans = []
    while pq:
        entry = heapq.heappop(pq)
        ans.append(entry[1])
    return ans

points = [[3,3]]
k = 1
print(kClosest(points,k))