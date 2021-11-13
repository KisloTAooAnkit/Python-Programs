def numOfCodes(arr,size):
    if(size==1 or size == 0):
        return 1
    
    output = numOfCodes(arr,size-1)
    if(arr[size-2]*10 + arr[size-1] <= 26):
        output += numOfCodes(arr,size-2)
    return output



def numOfCodesDP(arr,size,dp):
    if(size==1 or size == 0):
        return 1
    
    if(dp[size]>0):
        return dp[size]
    
    output = numOfCodes(arr,size-1)
    if(arr[size-2]*10 + arr[size-1] <= 26):
        output += numOfCodes(arr,size-2)
    dp[size] = output
    return output


def numOfCodes_i(arr,size):
    output = [0] * (size+1)
    output[0] = 1
    output[1] = 1

    for i in range(2,size):
        #output[i-x] represents it contains ans for remaining i-x elements in input arr
        output[i] = output[i-1]
        if(arr[i]*10 + arr[i-1] <= 26):
            output[i] += output[i-2]
        


num = [2,3,1,4]
dp = [0]*(len(num)+1)
print(numOfCodesDP(num,len(num),dp))