def monotoneIncreasing(n):
    x = n
    arr = []
    while(x>0):
        arr.append(x%10)
        x//=10
    
    arr = arr[::-1]
    dipIdx = -1
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            dipIdx = i-1
            break
    ans = 0

    if dipIdx == -1:
        for i in range(0,len(arr)):
            ans = ans*10 + arr[i]
        return ans

    while(dipIdx>0 and arr[dipIdx-1] == arr[dipIdx]):
        dipIdx-=1

    arr[dipIdx] -=1

    for i in range(dipIdx+1,len(arr)):
        arr[i] = 9

    for i in range(0,len(arr)):
        ans = ans*10 + arr[i]

    return ans

n =332
print(monotoneIncreasing(n))        

    