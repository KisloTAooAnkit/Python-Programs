from collections import defaultdict,deque

def accntMerge(accounts):
    ans = []
    graph = defaultdict(list)

    for account in accounts:
        n = len(account)
        for i in range(1,n):
            for j in range(1,n):
                graph[(account[0],account[i])].append(account[j])

    inQOrVisited = dict()
    for key,emailIDs in graph.items():
        if key[1] in inQOrVisited:
            continue
        arr = []
        q = deque()
        for email in emailIDs:
            q.append(email)
            
        
        while q:
            node = q.popleft()
            for email in graph[(key[0],node)]:
                if email not in inQOrVisited:
                    q.append(email)
                    inQOrVisited[email] = 1
                    arr.append(email)
        arr.sort()


        ans.append([key[0]]+arr)

    return ans    


accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","john00@mail.com","johnsmith@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
    ]

print(accntMerge(accounts))