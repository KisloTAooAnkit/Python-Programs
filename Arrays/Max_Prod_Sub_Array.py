


def maxProduct(arr):
    mainprod = 1
    otherproduct = 1
    flip = 1
    ans = 0
    n = len(arr)
    for i in range(0,n):
        if(flip == 1):
            val = mainprod*arr[i]
            if((val<0 and arr[i]<0 )or (val>0 and arr[i]>=0)):
                mainprod = val
            else:
                flip = 2
                mainprod = val
                otherproduct = arr[i]
        elif(flip ==2):
            val = mainprod*arr[i]
            val1 = otherproduct*arr[i]

            if(val>0):
                mainprod = val
                otherproduct = val1
            else:
                mainprod = val1
                otherproduct = val
            
        ans = max(mainprod,ans)
    
    print(ans)

a = [2,0,3,-2,4]
maxProduct(a)
