
def partitionLabels(s):
    dic = dict()

    n = len(s)
    for i in range(n-1,-1,-1):
        if s[i] not in dic:
            dic[s[i]] = i
    ans = []
    prevLen = -1
    maxRangeYet = 0
    for i in range(n):
        c = s[i]
        maxRangeYet = max(maxRangeYet,dic[c])
        if i == maxRangeYet:
            ans.append(maxRangeYet - prevLen)
            prevLen = maxRangeYet
    return ans


s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))


def dfs(node,dic):
    if node in dic:
        return dic[node]

    nnode = Node(node.val)
    res = []
    for nbr in node.neighbors:
        nnbr = dfs(nbr,dic)
        res.append(nnbr)
    
    nnode.neighbors = res
    return nnode


