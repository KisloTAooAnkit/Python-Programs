"""
Given an array of positive integers (ex: [2, 2, 3, 5, 2, 1, 1]), merge the smallest duplicate at each iteration until there are no more duplicates

Start - [2, 2, 3, 5, 2, 1, 1]
1st iteration (smallest duplicate = 1) - [2, 2, 3, 5, 2, 2]
2nd iteration (smallest duplicate = 2) - [4, 3, 5, 2, 2]
3rd iteration (smallest duplicate = 2) - [4, 3, 5, 4]
4th iteration (smallest duplicate = 4) - [3, 5, 8]

Note: Only [3, 5, 8] needs to be returned, we do not need the iterations along the way
"""



import heapq
from collections import defaultdict

def solution(arr):
    n = len(arr)
    pq = []
    for i in range(n):
        pq.append(arr[i])

    heapq.heapify(pq)
    ans = []
    
    while pq:
        currval = heapq.heappop(pq)
        nxtVal = pq[0] if pq else -1
        if currval == nxtVal:
            nxtVal = heapq.heappop(pq)
            heapq.heappush(pq,currval+nxtVal)
        else:
            ans.append(currval)
            
    return ans

arr = [2,2,3,5,2,1,1,1]
print(solution(arr))