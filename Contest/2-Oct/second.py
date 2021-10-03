

def maxCountOFTrues(arr,k):
    maxTrueCount = 0
    start = 0
    falseC = 0

    for end in range(0,len(arr)):
        if(arr[end] == "F"):
            falseC +=1
        
        while(falseC>k):
            if arr[start] == "F":
                falseC-=1
            start +=1
        maxTrueCount = max(maxTrueCount,end-start+1)
    return maxTrueCount

def maxCountOFFalse(arr,k):
    maxFalseCount = 0
    start = 0
    trueC = 0

    for end in range(0,len(arr)):
        if(arr[end] == "T"):
            trueC +=1
        
        while(trueC>k):
            if arr[start] == "T":
                trueC-=1
            start +=1
        maxFalseCount = max(maxFalseCount,end-start+1)
    return maxFalseCount


def sol(string,k):
    ans1 = maxCountOFTrues(string,k)
    ans2 = maxCountOFFalse(string,k)
    return max(ans1,ans2)

a = "TTFTTFTT"
k = 1

print(sol(a,k))