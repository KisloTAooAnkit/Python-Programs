def helper(s1,s2,count):
    if not s1 or not s2:
        return count

    if s1[0] == s2[0]:
        return helper(s1[1:],s2[1:],count+1)
    
    return max(
        helper(s1[1:],s2,0),
        helper(s1,s2[1:],0)
    )


def longestCommonSubstring(s1,s2):
    print(helper(s1,s2,0))

    
    
a = "ABCDGHF"
b = "ACDGHFR"
longestCommonSubstring(a,b)