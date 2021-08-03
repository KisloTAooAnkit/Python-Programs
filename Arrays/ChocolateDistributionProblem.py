import sys
def findMinDiff(a,m):
    a.sort()
    n = len(a)
    ans = sys.maxsize
    print(a)
    for i in range(0,n-m+1):
        print(a[i+m-1]-a[i],ans)
        ans = min(a[i+m-1]-a[i],ans) 
    return ans

a=[17, 83 ,59, 25, 38, 63, 25, 1, 37]
m = 9
print(findMinDiff(a,m))