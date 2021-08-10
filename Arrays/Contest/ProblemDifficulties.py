#https://www.codechef.com/AUG21C/submit/PROBDIFF

def solver(arr):
    n = len(arr)
    dic = dict()
    for i in range(0,n):
        if arr[i] in dic:
            dic[arr[i]] +=1
        else:
            dic[arr[i]] = 1
    
    for key in dic:
        if(dic[key]==3):
            return 1
        elif(dic[key]==2):
            return 2
        elif(dic[key] ==4):
            return 0
        
    return 2
        

test = int(input())
while(test):
    arr = list(map(int,input().strip().split()))
    print(solver(arr))


