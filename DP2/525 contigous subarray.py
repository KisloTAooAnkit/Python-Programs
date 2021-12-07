def sol(arr):
    rs = 0
    dic = dict()
    ans = 0
    n = len(arr)
    dic[0] = -1
    for i in range(n):
        if arr[i] == 1:
            rs +=1
        if arr[i] == 0:
            rs -=1
        if rs in dic:
            ans = max(ans,i-dic[rs])
        else:
            dic[rs] = i
    return ans

arr = [1,1,1,0,0,1,1,1,1,1]
arr = [0,1]
print(sol(arr))