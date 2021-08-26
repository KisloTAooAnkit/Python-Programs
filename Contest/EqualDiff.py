import sys
def solve(arr):

    dic = dict()
    n = len(arr)
    if(n==1):
        return 1
    if(n==2):
        return 0

    for i in range(n):
        if arr[i] not in dic:
            dic[arr[i]] =1
        else:
            dic[arr[i]] +=1
    
    
    mx = dic[max(dic, key=dic.get)]
    val = n - mx
    if(mx ==1 ):
        return val -1
    else:
        return val

test = int(input())
while(test):
    l = int(input())
    arr = list(map(int,input().strip().split()))
    print(solve(arr))
    test-=1
