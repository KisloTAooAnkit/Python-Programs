import heapq
def reorganizeString(s):
    hashmap = dict()
    for i in s:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] +=1
    ans = []
    pq = [(-freq,key) for key,freq in hashmap.items()]
    heapq.heapify(pq)
    prev_freq,prev_key = 0,""
    while(pq):
        freq,key = heapq.heappop(pq)
        ans.append(key)
        if prev_freq < 0:
            heapq.heappush(pq,(prev_freq,prev_key))
        #+1 kyunki -ve mein hai freq (min heap ko max heap jaise treat karna hai)
        freq +=1
        prev_freq,prev_key = freq,key
    ans = "".join(ans)
    if len(ans) < len(s):
        return ""
    return "".join(ans) 

s = "aaaabb"
print(reorganizeString(s))