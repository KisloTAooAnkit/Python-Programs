from collections import defaultdict
def dfs(i,dic,k,dp):
    if k == 0:
        return 0
    ans = 0
    if (i,k) in dp:
        return dp[(i,k)]
    cache = 0
    if i in dic:
        ans += dic[i]
        cache = dic[i]
        dic[i] = 0
    res2 = dfs(i-1,dic,k-1,dp)
    res1 = dfs(i+1,dic,k-1,dp)

    ans += max(res1,res2)
    dp[(i,k)] = ans
    return ans


def sol(fruits,startPos,k):
    dic = dict()
    dp = defaultdict(int)
    for pos,profit in fruits:
        dic[pos] = profit
    ans = dfs(startPos,dic,k,dp)

    return ans
fruits =[[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
startPos = 5
k = 4

print(sol(fruits,startPos,k))