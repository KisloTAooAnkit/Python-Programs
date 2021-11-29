from collections import deque
from collections import defaultdict
def sol(n,meetings,firstPerson):
    dic = defaultdict(list)
    for meeting in meetings:
        x,y,_ = meeting
        dic[x].append(y)
        dic[y].append(x)
    q = deque()
    q.append(firstPerson)
    ans = [0]
    hashmap = dict()
    while q:
        person = q.pop()
        hashmap[person] = 1
        for i in dic[person]:
            if i not in hashmap:
                q.append(i)
        if person != 0:
            ans.append(person)
    return ans

arr =  [[3,4,2],[1,2,1],[2,3,1]]
firstPerson = 1
print(sol(len(arr),arr,firstPerson))

        