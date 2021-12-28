#this is optimized recursive template yeha pe dp matrix nhi daala hai abhi but wohi 3D dp ka use karke ham bana skte hai axis would be n,x,tight


def solution(num,remainingLen,x,tight):
    if x <0:
        return 0
    if remainingLen == 1:
        if  0 <= x <10:
            return 1
        return 0
    
    ans = 0
    leftMostIdx = len(num) - remainingLen
    upperBound = int(num[leftMostIdx]) if tight else 9
    
    for i in range(0,upperBound+1):
        if i == upperBound and tight:
            ans += solution(num,remainingLen-1,x-i,tight)
        else:
            ans += solution(num,remainingLen-1,x-i,False)
    return ans

def solve(R,x):
    return solution(R,len(R),x,True)

R = "14354353453453453225"
x = 5
print(solve(R,x))


def solve(num,n,x,tight):
    if x < 0:
        return 0
    if n == 1:
        if 0 <= x <= 9:
            return 1
        return 0
    
    leftmostIdx = len(num) - n
    upperBound = int(num[leftmostIdx]) if tight else 9
    ans = 0
    for i in range(upperBound+1):
        
        if i == upperBound and tight:
            ans += solve(num,n-1,x-i,tight)
        else:
            ans += solve(num,n-1,x-i,False)
    return ans