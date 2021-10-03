from typing import AnyStr


def sol(arr,target):
    dic = dict()
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1
    ans = 0
    for substr in arr:
        dic[substr] -=1
        news = giveResString(target,substr)
        if news in dic:
            ans+=dic[news]
        dic[substr] +=1

    return ans

def giveResString(target,substr):
    target = list(target)
    substr = list(substr)
    idx = 0
    while((idx<len(substr) and idx<len(target)) and target[idx] == substr[idx]):
        idx+=1
    if idx < len(substr):
        return ""
    return "".join(target[idx:])
arr = ["4","4","43","34034","43403","4034"]


target = "434034"
print(sol(arr,target))