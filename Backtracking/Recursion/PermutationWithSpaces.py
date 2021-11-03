#https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1#


def permutation(string):
    ans = set()
    
    helper(string,"",len(string),ans)

    ans = list(ans)
    ans.sort()
    return ans



def helper(string,temp,n,ans):
    if(n==0):
        temp = temp.strip()
        ans.add(temp)
        return

    t1 =temp + " " + string[0]
    t2 = temp + string[0]
    helper(string[1:],t1,n-1,ans)
    helper(string[1:],t2,n-1,ans)
    return 


s = "AB"
print(permutation(s))