#https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1
def maxSumIS(arr, n):
    output=[0]*n
    output[0] = arr[0]
    for i in range(1,n):
        output[i] = arr[i]
        for j in range(i-1,-1,-1):
            if(arr[j]>=arr[i]):
                continue
            ans = arr[i] + output[j]
            if(output[i]<ans):
                output[i] = ans 
    print(output)
    return max(output)
	    

a = [13,14,14]
print(maxSumIS(a,len(a)))