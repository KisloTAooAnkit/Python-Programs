import math
def solver(n):
    for i in range(1, n+1):
        if(checkPrime(i)):
            print(i)

def checkPrime(number):
    rootval = int(math.sqrt(number))
    count = 0 
    for i in range(1,rootval+1):
        if number % i == 0:
            if i*i == number:
                count +=1
            else:
                count+=2
    
    if count > 2 :
        return False
    elif count == 2:
        return True
    else:
        return False 
    
solver(30)