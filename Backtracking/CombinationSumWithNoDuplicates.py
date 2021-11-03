from typing import Counter


def helper(idx,n,counterTable,ans,runningArr,targetSum):
    
    if targetSum<0:
        return
    if idx >=n:
        if 0 == targetSum:
            ans.append(runningArr[:])
        return
    
    if counterTable[idx][1] > 0:
        runningArr.append(counterTable[idx][0])
        counterTable[idx][1] -=1
        helper(idx,n,counterTable,ans,runningArr,targetSum-counterTable[idx][0])
        runningArr.pop()
        counterTable[idx][1] +=1

    helper(idx+1,n,counterTable,ans,runningArr,targetSum)
    return



def combinationSum2(arr,target):
    dic = Counter(arr)

    counterTable = [[val,freq] for val,freq in dic.items()]
    ans = []
    n = len(counterTable)
    helper(0,n,counterTable,ans,[],target)
    return ans

arr =   [10,1,2,7,6,1,5]
targt = 8
print(combinationSum2(arr,targt))
        

