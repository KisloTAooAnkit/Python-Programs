import heapq
def findMedian(arr):
    pq = [-1]
    #odd = 1 #even = 0
    cycle = 1
    n = len(arr)
    ans = []
    for i in range(n):
        val = arr[i]
        heapq.heappush(pq,val)
        if cycle == 1:
            heapq.heappop(pq)
            print(pq[0],end=" ")
            ans.append(pq[0])
        if cycle == 0:
            x = heapq.heappop(pq)
            med = (x + pq[0])//2
            print(med,end=" ")
            ans.append(med)
            heapq.heappush(pq,x)
        cycle = 1 - cycle
    return ans
arr = [5,4,3,2,1]
print(findMedian(arr))