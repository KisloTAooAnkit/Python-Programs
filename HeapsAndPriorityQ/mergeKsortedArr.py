import heapq
class HeapItem:
    def __init__(self,value,ri,ci,ei) -> None:
        self.value = value
        self.ri = ri
        self.ci = ci
        self.ei = ei

    def __lt__(self,other):
        return self.value < other.value


def mergeKSortedArr(matrix):
    pq = []
    ans = []
    #insert first row
    for idx,row in enumerate(matrix):
        hi = HeapItem(row[0],idx,0,len(row)-1)
        pq.append(hi)
    heapq.heapify(pq)

    while pq:
        item = heapq.heappop(pq)
        ans.append(item.value)
        item.ci = item.ci +1
        if item.ci <= item.ei:
            item.value = matrix[item.ri][item.ci]
            heapq.heappush(pq,item)
    return ans

