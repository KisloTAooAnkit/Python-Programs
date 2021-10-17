import heapq
def constructNumHeap(arr):
    num1 = 0
    num2 = 0
    heapq.heapify(arr)
    flag = True
    while(arr):
        val = heapq.heappop(arr)
        if flag:
            num1 = num1*10 + val
        else:
            num2 = num2*10 + val
        flag = not flag
    return num1 + num2

def constructNum(arr):

    arr.sort()

    num1 = 0
    num2 = 0
    flag = True
    for i in range(len(arr)):
        val = arr[i]
        if flag:
            num1 = 10*num1 + val
        else:
            num2 = 10*num2 + val
        flag = not flag
    
    return num1 + num2

arr = [5, 3, 0, 7, 4]

print(constructNum(arr))
