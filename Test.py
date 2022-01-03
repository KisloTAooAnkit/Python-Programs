def solve(s,k):
    s = list(s)
    n = len(s)
    odd = n%2 != 0
    unpair = 0
    left = n//2  - 1 if not odd else n//2
    right = n//2 
    while(left >=0 and right <n):
        if s[left] != s[right]:
            unpair +=1
        left -=1
        right +=1
    
    
    left ,right =0, n-1

    while(left<=right):
        if unpair > k:
            return -1

        if s[left] == s[right]:
            if left == right and k > 0:
                s[left] = "9"

            elif s[left] != "9" and k-2 >= unpair:
                s[left] = "9"
                s[right] = "9"
                k-=2

        elif k-2 >= unpair - 1:
            s[left] = "9"
            s[right] = "9"
            unpair -=1
            k-=2
        
        else:
            if s[left] < s[right]:
                s[left] = s[right]
            else:
                s[right] = s[left]
            unpair -=1
            k-=1

        left +=1
        right -=1
    
    return "".join(s)


s = "0011"
k = 1
print(solve(s,k))

    