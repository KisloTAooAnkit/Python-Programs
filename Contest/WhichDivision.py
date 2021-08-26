
def check(r):
    if(r>=2000):
        return 1
    if(1600<=r and r<2000):
        return 2
    if(r<1600):
        return 3 


test = int(input())
while(test):
    r = int(input())
    print(check(r))
    test-=1

