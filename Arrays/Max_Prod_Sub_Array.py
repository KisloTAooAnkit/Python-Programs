
import sys

def maxProduct(arr):
    # mainprod = 1
    # otherproduct = 1
    # flip = 1
    # ans = 0
    # n = len(arr)
    # for i in range(0,n):
    #     if(flip == 1):
    #         val = mainprod*arr[i]
    #         if((val<0 and arr[i]<0 )or (val>0 and arr[i]>=0)):
    #             mainprod = val
    #         else:
    #             flip = 2
    #             mainprod = val
    #             otherproduct = arr[i]
    #     elif(flip ==2):
    #         val = mainprod*arr[i]
    #         val1 = otherproduct*arr[i]

    #         if(val>0):
    #             mainprod = val
    #             otherproduct = val1
    #         else:
    #             mainprod = val1
    #             otherproduct = val
            
    #     ans = max(mainprod,ans)


    #O(n) sc and tc 
    n = len(arr)
    # minarr = [0]*n
    # maxarr = [0]*n
    # minarr[0] = maxarr[0] = arr[0]
    # for i in range(1,n):
    #     a = minarr[i-1]*arr[i]
    #     b= maxarr[i-1]*arr[i]
    #     c = arr[i]
    #     maxarr[i] = max(a,b,c)
    #     minarr[i] = min(a,b,c)
    # return max(maxarr)

    #O(n) tc O(1) sc
    maxans = arr[0]
    run_neg_prod = arr[0]
    run_pos_prod = arr[0]

    for i in range(1,n):
        a = arr[i]*run_neg_prod
        b = arr[i]*run_pos_prod
        c=arr[i]
        run_pos_prod = max(a,b,c)
        run_neg_prod = min(a,b,c)
        maxans = max(run_pos_prod,maxans)
    return maxans

a = [10,-2,4,-4,10,7,-10,1]
print(maxProduct(a))
