
def isSubset( a1, a2, n, m):
    dic = dict()
    if(m>n):
        for i in a2:
            if (i not in dic):
                dic[i] = 1
            else:
                dic[i] +=1
                
        for i in a1:
            if i in dic:
                dic[i] -=1
    else:
       return isSubset(a2,a1,m,n)
    for key in dic:
        if(dic[key] != 0):
            return "No"
    
    return "Yes"
            
a1 = [10, 5, 2, 23, 1]
a2 = [19, 5, 3]

print(isSubset(a1,a2,len(a1),len(a2)))