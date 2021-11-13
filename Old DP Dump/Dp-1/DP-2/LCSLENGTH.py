def lcs(s1,s2):
    if(len(s1) == 0 or len(s2)==0):
        return 0
    
    
    if(s1[0] == s2[0]):
        ans = 1 + lcs(s1[1:],s2[1:])
        return ans
    
    else:
        option1 = lcs(s1,s2[1:])
        option2 = lcs(s1[1:],s2)
        return max(option1,option2)
    


def lcs_I(s1,s2):
    m= len(s1)
    n= len(s2)
    dp =[[-1 for j in range(n+1)] for i in range(m+1)]
    
    for i in range(n+1):
        dp[0][i] = 0
        
    for j in range(m+1):
        dp[j][0] =0
        
    print(dp)
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(s1[m-i] == s2[n-j]):
                dp[i][j] = dp[i-1][j-1] + 1
            else :
                dp[i][j] = max(dp[i][j-1] , dp[i-1][j])
                
    return dp[m][n] 
    


def lcsDPhelper(s1,s2,m,n,dp):
    if(m ==0 or n==0):
        return 0
    
    if(dp[m][n] > -1):
        return dp[m][n]
    
    ans = 0
    #if both share same element at first index then we can say for sure that element is in lcs 
    if(s1[0] == s2[0]):
        ans = 1 + lcsDPhelper(s1[1:],s2[1:],m-1,n-1,dp)
    else:
        #considering first element of s1 is in lcs actually and first element of s2 is not hence 
        # then searching with next version of s2
        option1 = lcsDPhelper(s1,s2[1:],m,n-1,dp)
        
        #considering first element of s2 is in lcs actually and first element of s1 is not hence 
        # then searching with next version of s1
        option2 = lcsDPhelper(s1[1:],s2,m-1,n,dp)
        
        #taking out the maximum lcs length from both cases
        ans =  max(option1,option2)
        
    dp[m][n] = ans
    return ans



def lcsDP(s1,s2):
    m = len(s1)
    n = len(s2)
    dp =[[-1 for j in range(n+1)] for i in range(m+1)]
    return lcsDPhelper(s1,s2,m,n,dp)



 
a = "abcd"
b = "ad"   

print(lcs_I(a,b))
    
    
        