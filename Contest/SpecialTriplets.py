def sol(N):
    ans = []
    for a in range(1,N+1):
        for b in range(1,N+1):
            c = a%b 
            
            if(c!= 0 and b%c == 0):
                ans.append([a,b,c])
    
    print(ans)


def sol_one(N):
    ans = [0]*(N+1)
    for a in range(1,N+1):
        for b in range(1,a+1):
            c = a%b 
            d = b%a
            if(c!= 0 and b%c == 0):
                #print(a,b,c)
                ans[a] +=1

            if(d != 0 and a%d == 0):
                print(b,a,d)
                ans[a] +=1
        ans[a] += ans[a-1]        
    

    print(ans[-1])




N = 3
sol_one(4)
#sol(N)