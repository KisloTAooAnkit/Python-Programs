#https://leetcode.com/problems/next-greater-node-in-linked-list/

def performStack(arr,n):
    stack = []
    for i in range(0,n):
        val = arr[i]
        while(stack and stack[-1][0]<arr[i]):
            pair=stack.pop(-1)
            arr[pair[1]] = arr[i]
        stack.append((arr[i],i))
        arr[i] = 0
    return arr


def nextLargerNodes(head):
    temp = head
    arr = []
    while(temp):
        arr.append(temp.data)
    return performStack(arr,len(arr))

a = [73,74,75,71,69,72,76,73]

#print(performStack(a,len(a)))

def dailyTemperatures(T):
    n, right_max = len(T), float('-inf')
    res = [0] * n
    for i in range(n-1, -1, -1):
        t = T[i]
        if right_max <= t:
            right_max = t
        else:
            days = 1
            while T[i+days] <= t:
                days += res[i+days]
            res[i] = days
    return res

print(dailyTemperatures(a))