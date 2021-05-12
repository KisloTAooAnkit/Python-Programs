#https://leetcode.com/problems/uncrossed-lines/submissions/
#high priority : https://www.spoj.com/problems/BVAAN/ and https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

#after submission iske suggested problems dekhne hai - pending


def maxUncrossedLinesRec( arr1,arr2,m,n,dp):
        if(m == 0 or n==0):
            return 0
        if(dp[m][n]>-1):
            return dp[m][n]
        
        if(arr1[0] == arr2[0]):
            ans = 1 +   maxUncrossedLinesRec(arr1[1:],arr2[1:],m-1,n-1,dp)
            return ans
        else:
            option1 =   maxUncrossedLinesRec(arr1[1:],arr2,m-1,n,dp)
            option2 =   maxUncrossedLinesRec(arr1,arr2[1:],m,n-1,dp)
            ans = max(option1,option2)
            dp[m][n] = ans
            return ans

def maxUncrossedLines(A,B):
    m= len(A)
    n= len(B)
    dp = [[-1 for i in range(n+1)] for j in range(m+1) ]
    
    return   maxUncrossedLinesRec(A,B,m,n,dp)    

a = [2,5,1,2,5]
b=  [10,5,2,1,5,2]


print(maxUncrossedLines(a,b))
        

# (1,3,7,1,7,5) (1,9,2,5,1) 1+
#     (3,7,1,7,5) (9,2,5,1) min()
#         (7,1,7,5) (9,2,5,1) min(1,)
#             (1,7,5) (9,2,5,1) min(1,1) = 1
#                 (7,5) (9,2,5,1) min(1,1) =1 
#                     (5) (9,2,5,1) min(1,1) = 1
#                         () (9,2,5,1) = 0
                        
#                         (5) (2,5,1) min(0,1) =1
#                             () (2,5,1) = 0
                        
#                             (5) (5,1) 1+ 0 = 1
#                                 () (1) = 0

#                     (7,5) (2,5,1) min(1,1) = 1
#                         (5) (2,5,1) = 1

#                         (7,5) (5,1) min(1,0) =1
#                             (5) (5,1) = 1
                        
#                             (7,5) (1)  min(0,0) =0
#                                 (5) (1) min(0,0) =0
#                                     () (1) =0
                                    
#                                     (5) () =0

#                                 (7,5) () =0
                
#                 (7,5) (2,5,1) = 1
            
#             (1,7,5) (2,5,1) max(1,1) =1
#                 (7,5) (2,5,1) = 1
                
#                 (1,7,5) (5,1) max(1,1) =1
#                     (7,5) (5,1) = 1
                    
#                     (1,7,5) (1) = 1 + 0
#                         (1,7,5) () =0
                        
        
     
     
     
     
       
    #min ki jagah max
    # (1,2,4) (1,4,2) 1+1 = 2    
    #    (2,4) (4,2) min(1,1)
    
    #         (4) (4,2) 1
    
    #             () (2) 1+0 = 1
                
    #                 0
    
    #         (2,4) (2) 1 
    
    #             (4) () 1+ 0
    
    #                 0 
                
    
    # (1,2,3,7,6) (1,2,6,7,3) 1+2 = 3
    #     (2,3,7,6) (2,6,7,3) 1+1=2        
    #         (3,7,6) (6,7,3) min(1,1) = 1 
                
    #             (7,6) (6,7,3) min(1,1) = 1
    #                 (6) (6,7,3) 1 + 0 = 1
    #                     () (7,3) 0
                    
    #                 (7,6) (7,3) 1+0 = 1 
    #                     (6) (3) min(0,0) =0
    #                         (6) () 0
    #                         () (3) 0
                
    #             (3,7,6) (7,3) min(1,1) =1
                    
    #                 (7,6) (7,3) 1+0 =1 
    #                     (6) (3) min(0,0)
    #                         () (3) = 0
    #                         (6) () = 0 
                            
    #                 (3,7,6) (3) 1+ 0 = 1
    #                     (7,6) () 0

    
    
    