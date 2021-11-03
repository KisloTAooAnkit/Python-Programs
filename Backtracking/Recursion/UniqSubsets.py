#https://leetcode.com/problems/subsets-ii/
def subsetsUnique(arr):
    ans = []
    dic = dict()
    helper(arr,(),ans,len(arr),dic)
    res = []
    for i in ans:
        i = list(i)
        res.append(i) 
    del ans 
    return res


def helper(arr,temp,ans,n,dic):
    
    if ((n == 0) ):
        if (temp not in dic):
            dic[temp] = 1
            ans.append(temp)
        return 
    t1 = temp + (arr[0],)
    helper(arr[1:],t1,ans,n-1,dic)
    helper(arr[1:],temp,ans,n-1,dic)

    return 


#avoiding duplicates without any extra space also saving some recursive calls

def optimisedSol(arr):
    ans = []
    arr.sort()
    optimisedHelper(arr,[],ans)
    return ans


def optimisedHelper(arr,temp,ans):
    ans.append(temp)
    for i in range(len(arr)):
        if i>0 and arr[i-1] == arr[i]:
            continue
        optimisedHelper(arr[i+1],temp + [arr[i]],ans)



arr = [1,2,2]
print(subsetsUnique(arr))