def commonElements (A, B, C):
    i,j,k =0,0,0
    res = []
    while(i<len(A) and j<len(B) and k<len(C)):
        if(A[i] == B[j] and A[i] == C[k]):
            res.append(A[i])
            i+=1
            j+=1
            k+=1

        
        elif(A[i]<B[j] and A[i]<C[k]):
            i+=1
        
                
        elif(B[j]<A[i] and B[j]<C[k]):
            j+=1
        
                
        elif(C[k]<B[j] and C[k]<A[i]):
            k+=1
        
        
    return set(res) 


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]


print(commonElements(ar1,ar2,ar3))