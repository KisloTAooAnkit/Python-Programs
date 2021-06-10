def solution(arr,k):
    left =0 
    right = 0
    running_product = 1
    n= len(arr)
    total_subarrays = 0
    while(right<n):
        running_product = running_product * arr[right]

        while(running_product>=k):
            running_product //= arr[left]
            left+=1


        total_subarrays += right - left + 1

        right+=1
    
    return total_subarrays


nums = [10,5,2,6]
k = 100


print(solution(nums,k))



