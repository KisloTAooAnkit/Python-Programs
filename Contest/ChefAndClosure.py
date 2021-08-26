import builtins


def Solve(arr):
    minusonecount = 0
    onecount = 0
    bigcount = 0
    for i in arr:
        if (i==-1):
            minusonecount+=1
        if(i==1):
            onecount+=1
        if(abs(i)>1):
            bigcount +=1
    

    if(bigcount>1):
        return False
    if(minusonecount >=2 and onecount ==0):
        return False
    if(minusonecount >0 and bigcount>0):
        return False
    
    return True

arr = [1,3,3]
print(Solve(arr))