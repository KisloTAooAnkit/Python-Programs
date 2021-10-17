import heapq
def topKFreqElements(arr,k):
    dic = dict()
    for key in arr:
        if key not in dic:
            dic[key] =1
        else:
            dic[key] +=1
    
    kvp = [(freq,key) for key,freq in dic.items()]
    del dic
    pq = []
    for i in range(k):
        pq.append(kvp[i])
    
    heapq.heapify(pq)
    ans = []
    for i in range(k,len(kvp)):
        heapq.heappushpop(pq,kvp[i])
    
    while pq:
        ans.append(heapq.heappop(pq)[1])
    return ans

arr = [1]
k = 1
#print(topKFreqElements(arr,k))


def topKFreqQuickSelect(arr,k):
    dic = dict()
    for key in arr:
        if key not in dic:
            dic[key] =1
        else:
            dic[key] +=1
    
    kvp = [(key,freq) for key,freq in dic.items()]
    del dic
    n = len(kvp)
    start = 0
    end = n-1
    k = n - k
    ans = []
    while(start<=end):
        partIdx = partition(kvp,start,end)
        
        if partIdx == k:
            for i in range(k,n):
                ans.append(kvp[i][0])
            return ans
        if partIdx < k:
            start = partIdx +1
        else:
            end = partIdx-1
        
def partition(arr,low,high):
    pivot = arr[low]
    pivot_idx = low
    
    while(low<high):
        while(low<len(arr) and arr[low][1]<=pivot[1]):
            low+=1
        while(arr[high][1]>pivot[1]):
            high-=1
        if low < high:
            arr[low],arr[high] = arr[high],arr[low]
        
    arr[pivot_idx],arr[high] = arr[high],arr[pivot_idx]
    return high

arr = [4,1,1,2,2]
k = 1
print(topKFreqQuickSelect(arr,k))