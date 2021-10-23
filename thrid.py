import heapq
import math
def solution(b,a):
    for i,val in enumerate(a):
        a[i] = -val
    heapq.heapify(a)
    ans = 0
    while b > 0:
        val = heapq.heappop(a)
        ans += (val*-1)
        heapq.heappush(a,-math.floor((val*-1)/2))
        b-=1
    return ans


a =10
b = [ 2147483647, 2000000014, 2147483647 ]

print(solution(a,b))
