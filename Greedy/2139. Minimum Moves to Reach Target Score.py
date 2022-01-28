def solve(target,maxD):
    ans = 0
    while(target>1):
        if maxD == 0:
            ans += target -1
            target -= target-1
        elif target%2 == 0:
            target//=2
            maxD-=1
            ans +=1
        else:
            target -=1
            ans+=1
    return ans

t = 10
maxD = 4
print(solve(t,maxD))