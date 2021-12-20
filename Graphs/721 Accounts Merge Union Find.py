from collections import defaultdict
def findSuperParent(node,parent):
    if parent[node] == node:
        return node
    p = findSuperParent(parent[node],parent)
    parent[node] = p
    return p

def findUnion(node1,node2,rank,parent):
    s1 = findSuperParent(node1,parent)
    s2 = findSuperParent(node2,parent)
    if s1 != s2:
        if rank[s1]>rank[s2]:
            parent[s2] = s1
            rank[s1] += rank[s2]
            rank[s2] = 0
            return s1
        else:
            parent[s1] = s2
            rank[s2] += rank[s1]
            rank[s1] = 0
            return s2
    return s1
            
def solution(accounts):
    n = len(accounts)
    emailToId = defaultdict(int)
    parent = [i for i in range(n)]
    rank = [1]*n
    for id,account in enumerate(accounts):
        for email in account[1:]:
            if email not in emailToId:
                emailToId[email] = id
            else:
                oldGroup = emailToId[email]
                findUnion(id,oldGroup,rank,parent)
    
    IdToEmail = defaultdict(set)
    for email,id in emailToId.items():
        superParent = findSuperParent(id,parent)
        IdToEmail[superParent].add(email)
    ans = []
    for id in IdToEmail:
        emailList = sorted(list(IdToEmail[id]))                
        ans.append( [accounts[id][0]] + emailList)
    return ans

accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
            ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
            ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
            ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
            ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

ans = solution(accounts)
for account in ans:
    print(account)