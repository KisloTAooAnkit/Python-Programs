#https://practice.geeksforgeeks.org/problems/print-n-bit-binary-numbers-having-more-1s-than-0s0252/1#

def NbitBinary(N):
    ans = []
    helper(ans,"",N//2,0,N)
    return ans




def helper(ans,temp,zeroCount,onesCount,N):
    if(N==0):
        ans.append(temp)
        return 

    helper(ans,temp+"1",zeroCount,onesCount+1,N-1)
    if(zeroCount>0 and onesCount >0):
        helper(ans,temp+"0",zeroCount-1,onesCount,N-1)

    return    
    

n = 2

print(NbitBinary(n))