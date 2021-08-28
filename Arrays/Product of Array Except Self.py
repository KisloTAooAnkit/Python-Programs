#https://leetcode.com/problems/product-of-array-except-self/
def productExceptSelf(arr):
    n = len(arr)
    totalprod = 1
    zerocounter = 0
    for i in range(0,n):
        if(arr[i] == 0 and zerocounter == 0):
            zerocounter +=1
        elif(arr[i] ==0 and zerocounter >=1):
            return [0]*n
        else:
            totalprod *=arr[i]

    ans = [0]*n
    for i in range(0,n):
        if(zerocounter == 1 and arr[i] != 0):
            ans[i] =0
        elif(arr[i] == 0):
            ans[i] = totalprod
        else:
            ans[i] = totalprod // arr[i]
    return ans

def productExceptSelfWithoutDiv(arr):
    n = len(arr)
    ans = [1]* n
    ans1 = [1]*n 
    for i in range(1,n):
        ans[i] = arr[i-1]*ans[i-1]
    for i in range(n-2,-1,-1):
        ans1[i] = arr[i+1] * ans1[i+1]
    
    for i in range(0,n):
        ans[i] = ans[i]*ans1[i]
    
    return ans




arr = [-1,1,0,-3,3]
arr1 = [10, 3, 5, 6, 2]
print(productExceptSelf(arr))
print(productExceptSelfWithoutDiv(arr))