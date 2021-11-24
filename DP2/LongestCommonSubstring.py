def helper(s1,s2,count,ans):
    if not s1 or not s2:
        return 0

    if s1[0] == s2[0]:
        ans[0] = max(ans[0],count+1)
        return helper(s1[1:],s2[1:],count+1,ans)
    
    helper(s1[1:],s2,0,ans)
    helper(s1,s2[1:],0,ans)
    return
def helper(s1,s2,count,ans,dp,i1,i2,n1,n2):
    if n1==0 or n2==0:
        return 0
    if dp[]
    if s1[0] == s2[0]:
        ans[0] = max(ans[0],count+1)
        return helper(s1[1:],s2[1:],count+1,ans,dp)
    
    helper(s1,s2,0,ans,dp)
    helper(s1,s2,0,ans,dp)
    return



def longestCommonSubstring(s1,s2):
    ans = [0]
    helper(s1,s2,0,ans)
    print(ans)
    
a = "ABCDGH"
b = "ACDGHR"
longestCommonSubstring(a,b)