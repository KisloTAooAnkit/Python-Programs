def helper(ans,n,previousEle,k,runningString):
    if n == 0:
        k[0] -=1
        if k[0] == 0:
            ans[0] = runningString
        return
    for i in "abc":
        word = i
        if previousEle == word:
            continue
        helper(ans,n-1,word,k,runningString+word)
    return
        


def getHappyString(n,k):
    ans = [""]
    k = [k]
    helper(ans,n,"",k,"")
    return ans[0]

n=10
k = 100
getHappyString(n,k)