def dfs(n):
    if n== 0:
        return 0
    if n < 10:
        return 1
    ans2 = 0
    ans1 = dfs(n//10)
    val = n%100
    if val >=10:
        ans2 = dfs(n//100)
    return ans1 + ans2
    




def numDecodings(s):
    n = int(s)
    return dfs(n)

a = "06"
print(numDecodings(a))
    