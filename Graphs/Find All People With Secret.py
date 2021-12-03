from collections import deque
from collections import defaultdict
from itertools import groupby
#my wrong approach 38/42 TC passed
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
    groups = itertools.groupby(meetings,key=lambda x:x[2])
    print(groups)
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


def bfsSol(n,meetings,firstPerson):
    meetings.sort(key = lambda x: x[2])
    groups = groupby(meetings , key=lambda x : x[2])

    ans = {0,firstPerson}
    for time , group in groups:
        knows = set()
        graph = defaultdict(list)
        for x,y,t in group:
            graph[x].append(y)
            graph[y].append(x)
            if x in ans:
                knows.add(x)
            if y in ans:
                knows.add(y)

        queue = deque(knows)
        while queue:
            item = queue.pop()
            for neighbours in graph[item]:
                if neighbours not in ans:
                    ans.add(neighbours)
                    queue.append(neighbours)
    return list(ans)