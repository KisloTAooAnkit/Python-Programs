import BuildTreeFromStr
def kHelper(root,k,path):
    if not root:
        return
    path.append(root.data)
    kHelper(root.left,k,path)
    kHelper(root.right,k,path)
    checkForSum(path,k)
    path.pop()
    return    
    

def checkForSum(path,k):
    runningSum = 0
    n = len(path)
    for i in range(n-1,-1,-1):
        runningSum += path[i]
        if runningSum == k:
            for j in range(i,n):
                print(path[j],end=" ")
            print()

def printKSumPaths(root,k):
    path = []
    kHelper(root,k,path)

n = "null"
k=5
arr =[1,3,-1,2,1,4,5,n,n,1,n,1,2,n,6]
root = BuildTreeFromStr.buildTree(arr)
printKSumPaths(root,k)