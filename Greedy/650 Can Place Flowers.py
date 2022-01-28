
def canPlaceFlowers(arr,flowers):
    n = len(arr)
    rightSide = [0]*n
    lastOneIdx = n+1
    for i in range(n-1,-1,-1):
        if arr[i] == 1:
            lastOneIdx = i
            continue
        rightSide[i] = abs(i-lastOneIdx)
    
    lastOneIdx = -2

    for i in range(n):

        if arr[i] == 1:
            lastOneIdx = i
            continue
        lgap = i - lastOneIdx
        rgap = rightSide[i]
        if lgap >1 and rgap > 1:
            flowers -=1
            lastOneIdx = i
        if flowers == 0:
            return True
    return flowers == 0

def canPlaceFlowersOpt(arr,flowers):

    n = len(arr)
    for i in range(n):
        if flowers <= 0:
            return True
        if arr[i] == 1:
            continue
        prev = 0 if i-1 < 0 else arr[i-1]
        nxt = 0 if i+1 >=n else arr[i+1]
        if prev == 0 and nxt == 0:
            flowers -=1
            arr[i] = 1
    return flowers <= 0

flowerBed = [1,0,0,0,0] 
n = 1

print(canPlaceFlowers(flowerBed,n))

    
