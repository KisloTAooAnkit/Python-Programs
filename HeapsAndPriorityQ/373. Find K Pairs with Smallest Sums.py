import heapq
def kSmallestPairs(arr1,arr2,k):
    pq = []
    pq.append((arr1[0] + arr2[0],0,0))
    heapq.heapify(pq)
    ans = []
    visited = dict()
    visited[(0,0)] = 1
    while k:
        _,x,y = heapq.heappop(pq)
        ans.append([arr1[x],arr2[y]])

        if x+1 < len(arr1) and (x+1,y) not in visited:
            heapq.heappush(pq,(arr1[x+1]+arr2[y],x+1,y))
            visited[(x+1,y)] = 1
        
        if y+1 < len(arr2) and (x,y+1) not in visited:
            heapq.heappush(pq,(arr1[x]+arr2[y+1],x,y+1))
            visited[(x,y+1)] = 1
        k-=1
    return ans


nums1 = [1,1,2]
nums2 = [2,4,6]
k = 3
print(kSmallestPairs(nums1,nums2,k))

        



