import heapq
def minimizeRopsCost(arr):
    n = len(arr)
    heapq.heapify(arr)
    ans = 0
    while(len(arr)>=2):
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        ans += first + second
        heapq.heappush(arr,first+second)
    return ans

arr = [4, 2, 7, 6, 9]
print(minimizeRopsCost(arr))
        