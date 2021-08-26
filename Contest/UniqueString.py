def generateAllBinaryStrings(n, string, i,dic):
 
    if(string in dic):
        return True
    
    if i == n:
        print(string)
        return False
    
     
    if(generateAllBinaryStrings(n, string+"0", i + 1,dic) and generateAllBinaryStrings(n, string+"1", i + 1,dic)):
        return True
    else:
        return False

def solve(dic,N):
    generateAllBinaryStrings(N,"",0,dic)


test = int(input())
while(test):
    mydic = dict()
    N = int(input())
    for i in range(N):
        s = input()
        mydic[s] = 1
    solve(mydic,N)
    test-=1
