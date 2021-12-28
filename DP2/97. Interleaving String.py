from collections import defaultdict
def dfs(s1,s2,s3,n1,n2,n3,dp):
    if n3 == 0:
        if n1 == 0 and n2 ==0:
            return True
        return False
    
    if dp[(n1,n2,n3)] > -1:
        return dp[(n1,n2,n3)]

    ans = False
    if n1>0 and s1[0] == s3[0]:
        ans = ans or dfs(s1[1:],s2,s3[1:],n1-1,n2,n3-1,dp)
    if n2>0 and s2[0] == s3[0]:
        ans = ans or dfs(s1,s2[1:],s3[1:],n1,n2-1,n3-1,dp)
    dp[(n1,n2,n3)] = ans
    return ans

def iterative(s1,s2,s3):
    n1,n2,n3 = len(s1),len(s2),len(s3)
    dp = [[0]*(n2) for _ in range(n1)]
    


def isInterLeave(s1,s2,s3):
    n1,n2,n3 = len(s1),len(s2),len(s3)
    dp = defaultdict(lambda : -1)
    
    return dfs(s1,s2,s3,n1,n2,n3,dp)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterLeave(s1,s2,s3))