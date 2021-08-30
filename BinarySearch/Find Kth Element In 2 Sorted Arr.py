
import sys
def kthElement(arr1,arr2,n,m,k):
    
    
    if(n>m):
        return kthElement(arr2,arr1,m,n,k)
    low = max(0,k-m)
    high = min(n,k)
    
    while(low<=high):
        cut1 = low + (high-low)//2
        cut2 = k - cut1
    
        left1 = -sys.maxsize if cut1 == 0 else arr1[cut1-1]
        left2 = -sys.maxsize if cut2 ==  0 else arr2[cut2-1]
        
        right1 = sys.maxsize if cut1 == n else arr1[cut1]
        right2 = sys.maxsize if cut2 == m else arr2[cut2]
        
        
        if(left1<=right2 and left2 <= right1):
            return max(left1,left2)

        elif(left1>right2):
            high = cut1 - 1
        else:
            low = cut1 + 1
            
            
    return 0 



a = [2,3,6,7,9]
b = [1,4,5,8,10]
k = 2
print(kthElement(a,b,len(a),len(b),k))