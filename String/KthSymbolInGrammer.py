def kthGrammar(n,k):
    if(n==1 or k ==1):
        return 0
    
    noe = 2**(n-1)
    mid = noe//2
    
    if(k>mid):
        ans = kthGrammar(n-1,k-mid)
        return 1 - ans
    elif(k<=mid):
        return kthGrammar(n-1,k)
    
print(kthGrammar(3,1))
