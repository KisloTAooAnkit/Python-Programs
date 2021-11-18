
def solution():
    boxCount = int(input())
    boxes = [0]*(boxCount+1)
    numberOfDays = int(input())
    while(numberOfDays):
        l,r = list(map(int,input().strip().split()))
        boxes[l] +=1
        boxes[r+1] -=1
        numberOfDays-=1

    for i in range(boxCount):
        if i==0:
            continue
        boxes[i] = boxes[i-1] + boxes[i]

    n = max(boxes)
    dp = [0]*(n+2)
    for i in boxes:
        if i == 0:
            continue
        dp[1] +=1
        dp[i+1] -=1
    for i in range(n+2):
        if i ==0:
            continue
        dp[i] = dp[i-1] + dp[i]
    qryCount = int(input())
    while qryCount:
        x = int(input())
        if x > n:
            print(0)
        else:
            print(dp[x])
        qryCount-=1
solution()