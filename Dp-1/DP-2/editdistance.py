#HARD PROBLEM
#https://leetcode.com/problems/edit-distance/


#Approach similar to LCS and delete_operation in two strings but here we count at the time we perform operation 
# # and there are 3 possible cases we have to monitor 


# base case: word1 = "" or word2 = "" => return length of other string

# recursive case: word1[0] == word2[0] => recurse on word1[1:] and word2[1:]

# recursive case: word1[0] != word2[0] => recurse by inserting, deleting, or replacing 

#further details in the code

def editDistance(s1,s2,m,n):
    #if both length are zero no need of operation
    if(m==0 and n==0):
        return 0
    
    #if word1 is zero then we have to insert len(word2) elements 
    if(m==0):
        return n
    
    #if target string word2 is zero then we have to remove len(word1) elements
    if(n==0):
        return m
    
    #if matching element if found at first letter of both string -> move ahead 
    if(s1[0] == s2[0]):
        return editDistance(s1[1:],s2[1:],m-1,n-1)
    
    else:
        #replace : exchanging word1[0] with word2[0]
        temp = s2[0] + s1[1:]
        option1 = 1 + editDistance(temp,s2,m,n)
        
        #remove : removing word1[0]
        temp = s1[1:]
        option2 = 1 + editDistance(temp,s2,m-1,n)
        
        #insert : inserting word2[0]
        temp = s2[0] + s1[:]
        option3 = 1 + editDistance(temp,s2,m+1,n)
        
        #taking out the minimum
        return (min(option1,option2,option3))
    
    
def editDistanceDP(s1,s2,m,n,dp):
    if(m==0 and n==0):
        return 0
    if(m==0):
        return n
    if(n==0):
        return m
    
    
    if(dp[m][n]>-1):
        return dp[m][n]
    
    if(s1[0] == s2[0]):
        return editDistanceDP(s1[1:],s2[1:],m-1,n-1,dp)
    
    else:
        #replace
        temp = s2[0] + s1[1:]
        option1 = 1 + editDistanceDP(temp,s2,m,n,dp)
        
        #remove
        temp = s1[1:]
        option2 = 1 + editDistanceDP(temp,s2,m-1,n,dp)
        
        #insert
        temp = s2[0] + s1[:]
        option3 = 1 + editDistanceDP(temp,s2,m+1,n,dp)
        
        ans = (min(option1,option2,option3))
        dp[m][n] = ans
        return ans
    
    
a= "abcedshghchgcggfgrdgvjbkjbhjgfvgsdsdsdsd"
b= "asdebsahgghvghcgfdhfgrs"
print(a,b)

def caller(a,b):
    m = len(a)
    n = len(b)
    dp = [[-1 for j in range(n+1)] for i in range (m+n+1)]
    return editDistanceDP(a,b,m,n,dp)   

print(caller(a,b))
print(editDistance(a,b,len(a),len(b)))

        
        