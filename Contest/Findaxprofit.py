def foo(arr,n):
    k = len(arr)
    arr.sort()
    cost =[0]*k
    for i in range(k):
        cost[i] = arr[i][1] - arr[i][0] + arr[i][2]
    for i in range(1,k):
        currmax = cost[i]
        for j in range(i-1,-1,-1):
            if (arr[j][1] <= arr[i][0]):
                val = cost[i] + cost[j]
                if val > currmax:
                    currmax = val
        cost[i] = currmax
    return max(cost)


a =  [[2,5,4],[1,5,1]]
print(foo(a,10))