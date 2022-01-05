
def helper(s1,s2,dp):
    n = len(s1)
    key = (s1,s2)
    if n <= 0:
        return True
    
    if s1 == s2:
        return True
    
    if key in dp:
        return dp[key]
    
    for k in range(1,n):
        ##### 1st case if string is scrambled #####
        if (helper(s1[:k],s2[n-k:],dp) and helper(s1[k:],s2[:n-k],dp)):
            dp[key] = True
            return True
        if (helper(s1[:k],s2[:k],dp) and helper(s1[k:],s2[k:],dp)):
            dp[key] = True
            return True
    dp[key] = False
    return False
        



def scrambledString(s1,s2):
    if len(s1) != len(s2):
        return False
    dic = dict()
    return helper(s1,s2,dic)


s1 = "great"
s2 = "rgeat"
print(scrambledString(s1,s2))
