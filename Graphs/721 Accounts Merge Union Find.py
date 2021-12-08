from collections import defaultdict

def getParent(node,parent):
    if node == parent[node]:
        return node
    return getParent(parent[node],parent)

def unionFind(node1,node2,parent):
    parent1 = getParent(node1,parent)
    parent[node2] = parent1
    return parent1

def sol(accounts):
    n = len(accounts)
    parent = [i for i in range(n)]
    email_ParentMap = defaultdict(int)
    for currparent,account in enumerate(accounts):
        cache = currparent
        for idx,email in enumerate(account):
            if idx ==0:
                continue
            if email not in email_ParentMap:
                email_ParentMap[email] = cache
            else:
                #union find and update parent array
                otherParentWithSameEmail = email_ParentMap[email]
                cache = unionFind(otherParentWithSameEmail,currparent,parent)
    
    #process Parent array:
    ans = []
    n = 0
    emailVisited = defaultdict(int)
    for currparent,account in enumerate(accounts):
        rootParent = parent[currparent]
        emails = account[1:]
        emails.sort()
        
        if n<=rootParent:
            ans.append([account[0]]+emails)
            for idx,email in enumerate(emails):
                if email not in emailVisited:
                    emailVisited[email] = 1
            n+=1
        else:
            for idx,email in enumerate(emails):
                if email not in emailVisited:
                    ans[rootParent].append(email)
                    emailVisited[email] = 1
    return ans
    
                
    


accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","john00@mail.com","johnsmith@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
    ]

print(sol(accounts))