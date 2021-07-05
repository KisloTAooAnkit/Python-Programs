def solution(arr):
    arr.sort()
    if(len(arr)<=1):
        return 0

    result = 0

    prev = 0
    
    for i in range(1,len(arr)):
        prev_meeting = arr[prev]
        curr_meeting = arr[i]

        if(prev_meeting[1]>curr_meeting[0]):
            result+=1

        prev = prev if prev_meeting[1] < curr_meeting[1] else i 

    return result


arr =[[1,2],[1,2],[1,2]]

print(solution(arr))