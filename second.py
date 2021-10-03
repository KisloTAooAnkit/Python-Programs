def split(x, n,ans):
 

    if(x < n):
        print(-1)
 

    elif (x % n == 0):
        for i in range(n):
            ans.append(x//n)
    else:

        zp = n - (x % n)
        pp = x//n
        for i in range(n):
            if(i>= zp):
                ans.append(pp+1)
            else:
                ans.append(pp)


def solution(arr,mean,n):
    m = len(arr)
    s = sum(arr)
    x = mean*(m+n) - s
    ans = []
    split(x,n,ans)
    for i in ans:
        if i > 6:
            return []
    return ans

a = [3,2,4,3] 
mean = 4
n= 2
print(solution(a,mean,n))
