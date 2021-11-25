def maxDiffUsingKadane(s):
    n = len(s)
    ans = float("-inf")
    maxSoFar = float("-inf")
    for i in range(n):
        if s[i] == "1":
            maxSoFar = max(-1,maxSoFar-1)
        if s[i] == "0":
            maxSoFar = max(1,maxSoFar+1)
        ans = max(ans,maxSoFar)
    return ans

s = "111111"
print(maxDiffUsingKadane(s))