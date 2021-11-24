

def countSubarrays(arr,k):
    if k <=1:
        return 0
    prod = 1
    left = 0
    right = 0
    n = len(arr)
    ans = 0
    while(right<n):
        prod = prod*arr[right]
        while prod>=k:
            prod = prod//arr[left]
            left+=1
        ans = right - left +1
        right +=1
    return ans

