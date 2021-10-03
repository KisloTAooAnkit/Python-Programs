def solution(arr,m,n):
    if len(arr) != (m*n):
        return []
    
    ans = []
    start = 0
    end = n-1
    for i in range(m):
        sub = arr[start : start + n]
        start += n        
        ans.append(sub)
    return ans


a=[1,2,3]
m = 1
n = 3

print(solution(a,m,n))