def lcs_string(s1,s2,m,n,dp):
    if(m ==0 or n==0):
        return ""
    
    res = ""
    if (m,n) in dp:
        return dp[(m,n)]
    
    if(s1[0] == s2[0]):
        res = res + s1[0] + lcs_string(s1[1:],s2[1:],m-1,n-1,dp)
        
    else:
        option1 = lcs_string(s1[1:],s2,m-1,n,dp)
        option2 = lcs_string(s1,s2[1:],m,n-1,dp)
        if(len(option1)>len(option2)):
            res = res + option1
        else:
            res = res + option2
        
        dp[(m,n)] = res    
        
    return res


#fails at this case
a="aaaaaazzzz"
b="zzzzaaaaaa"  
n=4
def BVAAN(a,b,n):
    dp = {}
    res = lcs_string(a,b,len(a),len(b),dp)
    ans = 0
    if(len(res)>=n):
        res = "".join(sorted(res,reverse=True))
        print(res)
        for i in range(n):
            ans += ord(res[i])
        return ans 
    else:
        return 0
    
print(BVAAN(a,b,n))
        