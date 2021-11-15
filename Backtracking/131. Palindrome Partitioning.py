def isArrPalindrome(arr):
    count = 0
    for word in arr:
        if word == word[::-1]:
            count+=1
    return count == len(arr)


def helper(s,arr,ans):
    if len(s) == 0:
        if isArrPalindrome(arr):
            ans.append(arr[:])
        return
    
    n = len(s)
    for i in range(n):
        newString = s[i+1:] if i+1 < n else ""
        arr.append(s[:i+1])
        helper(newString,arr,ans)
        arr.pop()
    return




def partition(s):
    ans = []
    helper(s,[],ans)
    return ans
s = "aaabccc"
print(partition(s))