import heapq

def solve(arr,hp,teleports):
    i = 1
    pq = []
    n = len(arr)
    while(i<n):
        hpCost = arr[i] - arr[i-1] 
        hp -=hpCost
        heapq.heappush(pq,-hpCost)
        while(pq and teleports>0 and hp < 0):
            val = -heapq.heappop(pq)
            teleports-=1
            hp += val
        if hp < 0:
            break
    return i-1 + 1
            