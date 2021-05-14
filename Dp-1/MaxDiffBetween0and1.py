
#https://practice.geeksforgeeks.org/problems/maximum-difference-of-zeros-and-ones-in-binary-string4111/1

def maxDiff(s):
    n= len(s)
    output=[0]*n
    output[0] = 1 if s[0] == "0" else 0
    for i in range(1,n):
        if(s[i]=="0"):
            output[i] = output[i-1] + 1
        if(s[i]=="1"):
            x = output[i-1] -1
            output[i] = 0 if x <0 else x
    
    ans = max(output)
    return -1 if ans == 0 else ans



s = "11000001000011101"

print(maxDiff(s))