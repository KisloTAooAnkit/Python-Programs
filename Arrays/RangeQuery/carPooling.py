import heapq
def carPooling(trips,capacity):
    maxdist = 0
    for trip in trips:
        _,to,frm = trip
        maxdist = max(frm,maxdist)
    maxdist = maxdist+2
    diffarr = [0]*(maxdist)

    for trip in trips:
        count,to,frm = trip
        diffarr[to] += count
        diffarr[frm] -= count
    
    for i in range(maxdist):
        if i ==0:
            continue
        diffarr[i] = diffarr[i-1] + diffarr[i]
    
    for i in range(maxdist):
        if diffarr[i]>capacity:
            return False
    return True

def carPoolingHeap(trips,capacity):
    trips.sort(key=lambda x:(x[1],x[2]))

    pq = [] #(end,num)
    total = 0
    for num,s,e in trips:
        while pq and pq[0][0] <= s:
            total -= heapq.heappop(pq)[1]
        heapq.heappush(pq,(e,num))
        total += num
        if total > capacity:
            return False


trips = [[5,4,7],[7,4,8],[4,1,8]]

capacity = 17
print(carPooling(trips,capacity))
