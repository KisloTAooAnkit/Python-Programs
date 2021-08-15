import sys
def longestPalindrome(string):
    n = len(string)
    dp = [[False for j in range(n)] for i in range(n)]
    maxstring = ""

    for gap in range(0,n):
       j = gap
       i=0
       while(j<n):
            if(gap == 0):
               dp[i][j] = True
               
               maxstring = string[i]
            elif(gap ==1):
                if(string[i] == string[j]):
                    dp[i][j] = True
                    maxstring = string[i:j+1]

            else:
                if(string[i] == string[j] and dp[i+1][j-1] == True):
                    dp[i][j] = True

                    maxstring = string[i:j+1]

                    
            
            i+=1
            j+=1
    
    return maxstring

s = "cbbd"
print(longestPalindrome(s))