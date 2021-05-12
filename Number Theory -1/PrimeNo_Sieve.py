import math

#complexity : N log log N

def solver(n):
    sieve = [True]*(n+1)
    sieve[0],sieve[1] = False,False
    lastIndex = int(math.sqrt(n))
    for i in range(2,lastIndex+1):
        if sieve[i]:
            for j in range(i,n+1):
                currindex = j*i
                if(currindex>n):
                    break
                sieve[currindex] = False
    
    for i in range(0,n+1): 
        if sieve[i]:
            print(i,end=" , ")

    
solver(100)