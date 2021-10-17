from queue import PriorityQueue

q = PriorityQueue()
q.put(12)
q.put(6)
q.put(5)
q.put(100)
q.put(1)
q.put(9)
q.put(0)
q.put(14)
while not q.empty():
    print(q[0][1])
    ans = q.get()
    print(ans,end=" ")