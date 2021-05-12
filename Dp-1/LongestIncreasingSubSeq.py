
'''
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such 
that all elements of the subsequence are sorted in increasing order. 
For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
'''


def LIS(arr,n):
    output = [0]*n
    output[0] = 1
    for i in range(1,n):
        output [i] = 1
        for j in range(i-1,-1,-1):
            if(arr[j]>arr[i]):
                continue
            possibleAns = output[j] + 1
            if(output[i]<possibleAns):
                output[i] = possibleAns
                
    best = 0
    for i in range(n):
        if(best<output[i]):
            best = output[i]

    return best

arr = [0,1,3,4,9,7,8]

print(LIS(arr,len(arr)))

    
    
            