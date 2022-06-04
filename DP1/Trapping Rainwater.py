def trappingRainwater(arr):
    n = len(arr)
    left = 0
    right = n-1

    ans = 0
    leftMax = arr[left]
    rightMax = arr[right]
    while(left <= right):
        leftMax = max(leftMax,arr[left])
        rightMax = max(rightMax,arr[right])

        if leftMax < rightMax:
            ans += leftMax - arr[left]
            left +=1
        else:
            ans += rightMax - arr[right]
            right -=1
    return ans