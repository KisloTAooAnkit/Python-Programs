from collections import deque
def firstNegInt(arr,n,k):
    q = deque()
    temp = []
    start = 0
    end = 0

    while(end<n):
        if arr[end] < 0 :
            q.append(arr[end])
        while(end - start + 1 == k):
            temp.append(0 if not q else q[0])
            if q and arr[start] == q[0]:
                
                q.popleft()
            start +=1
        end+=1
    return temp

a = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
n = len(a)
print(firstNegInt(a,n,k))