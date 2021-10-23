

import heapq
class HeapItem:
    def __init__(self,value,ri,ci,ei) -> None:
        self.val = value
        self.ri = ri
        self.ci = ci
        self.ei = ei
    
    def __lt__(self,other):
        return self.val < other.val
        

def smallestRange(matrix):
    minHeap = []
    maxele = float("-inf")

    for idx,row in enumerate(matrix):
        item = HeapItem(row[0],idx,0,len(row)-1)
        maxele = max(maxele,row[0])
        minHeap.append(item)
    
    heapq.heapify(minHeap)
    mindiff = float("inf")
    ans = [0,0]
    while minHeap:
        item = heapq.heappop(minHeap)
    
        if maxele - item.val < mindiff:
            mindiff = maxele - item.val
            ans = [item.val,maxele]
    
        item.ci = item.ci +1
    
        if item.ci <= item.ei:
            item.val = matrix[item.ri][item.ci]
            maxele = max(maxele,item.val)
            heapq.heappush(minHeap,item)
    
        else:
            break

    return ans


matrix = [[1],[2],[3],[4],[5],[6],[7]]
print(smallestRange(matrix))