def ngr(arr1,arr2):
    stack = [arr2[0]]
    dic = dict()
    n1 = len(arr1)
    n2 = len(arr2)
    for i in range(1,n2):
        while(stack and stack[-1] < arr2[i]):
            val = stack.pop()
            dic[val] = arr2[i]
        stack.append(arr2[i])
    while(stack):
        val = stack.pop()
        dic[val] = -1


    ans = [0]*n1
    for key,val in enumerate(arr1):
        ans[key] = dic[val]
    return ans

a1 = [2,4]
a2 = [1,2,3,4]
print(ngr(a1,a2))

    