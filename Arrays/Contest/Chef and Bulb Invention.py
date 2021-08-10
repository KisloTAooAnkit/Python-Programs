#https://www.codechef.com/AUG21C/problems/CHFINVNT
"""Getting wrong answer"""
def solution(n,p,k):
    multiples = ((n-1) // k ) + 1
    
    # if(p>=n):
    #     return 0
    # if(p==0):
    #     return 1
    # if(p%k ==0):
    #     return 1 + (p//k)
    
    # if(p<k):
    #     return (p*multiples) +1
    # if(p>k):
    return ((p%k) * multiples) + ((p//k) +1)
        
# test = int(input())
# while(test):
#     data = list(map(int,input().strip().split()))
#     print(solution(data[0],data[1],data[2]))
#     test-=1

print(solution(40,12,13))
