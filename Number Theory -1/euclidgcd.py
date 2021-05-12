def GCD(a,b):
    if(a<b):
        GCD(b,a)
    if(b==0):
        return a 
    return GCD(b,a%b)
    

print(GCD(100,6))