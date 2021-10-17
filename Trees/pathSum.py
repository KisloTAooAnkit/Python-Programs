def pathSumBruteForce(root,runningPath,count,target):
    if not root:
        return 
    runningPath.append(root.data)

    pathSumBruteForce(root.left,runningPath,count,target)
    pathSumBruteForce(root.right,runningPath,count,target)
    updateCount(runningPath,target,count)
    runningPath.pop()
    return

def updateCount(arr,target,count):
    runningSum = 0
    n = len(arr)
    for i in range(n-1,-1,-1):
        runningSum += arr[i]
        if runningSum == target:
            count[0] +=1

def pathSumCallerOld(root,target):
    count = [0]
    path = []
    pathSumBruteForce(root,path,count,target)
    return count[0]




def pathSumOpt(root,hash,runningsum,ans,target):
    if not root:
        return
    runningsum += root.val
    redundantSum = runningsum - target
    ans[0] += hash.get(redundantSum,0)
    if runningsum in hash:
        hash[runningsum] +=1
    else:
        hash[runningsum] = 1
    pathSumOpt(root.left,hash,runningsum,ans,target)
    pathSumOpt(root.right,hash,runningsum,ans,target)
    hash[runningsum] -=1
    return
     
def pathSumCallerNew(root,target):
    dic = {0:1}
    ans = [0]
    runningSum = 0
    pathSumOpt(root,dic,runningSum,ans,target)
    return ans[0]    

