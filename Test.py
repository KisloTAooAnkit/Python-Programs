from collections import deque
from collections import defaultdict
def sol(n,meetings,firstPerson):
    dic = defaultdict(list)
    for meeting in meetings:
        x,y,time = meeting
        dic[(x,time)].append(y)
        dic[(y,time)].append(x)
    print(dic)
    knows = dict()
    knows[0] = 1
    knows[firstPerson] = 1
    meetings.sort(key = lambda x:x[2])
    ans = []
    ans.append(0)
    ans.append(firstPerson)
    for i in range(len(meetings)):
        x,y,time = meetings[i]
        if x in knows:
            for person in dic[(x,time)]:
                if not person in knows:
                    knows[person] = 1
                    ans.append(person)
        elif y in knows:
            for person in dic[(y,time)]:
                if not person in knows:
                    knows[person] = 1
                    ans.append(person)
    return ans

n = 7336

firstPerson = 1
meetings = [[0,2,1],[1,3,1],[4,5,1]]
print(sorted(sol(n,meetings,firstPerson)))