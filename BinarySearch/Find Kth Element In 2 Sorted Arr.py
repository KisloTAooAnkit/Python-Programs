
import sys
def kthElement(arr1,arr2,n,m,k):
    
    #always treat lower len array as arr1
    if(n>m):
        return kthElement(arr2,arr1,m,n,k)
    #to handle edge case:
    #in general case ham 1st array se zero pick krste hai but in case 
    # a1 = 7 12 14 15
    # a2 = 1  2  3  4  9 11  and k = 7
    # is case mein hame peheli array se ek element pick karna hi hoga  
    low = max(0,k-m)
    #similarly in case k<n hai then we can pick max no elements from arr1 is k only otherwise 
    # n hoga
    high = min(n,k)
    
    while(low<=high):
        #cut represents number of elements before that cut 
        cut1 = low + (high-low)//2
        #remaining elements for 2nd array
        cut2 = k - cut1

        #edge handling incase cut extreme ends pe horhe ho toh left side -inf 
        left1 = -sys.maxsize if cut1 == 0 else arr1[cut1-1]
        left2 = -sys.maxsize if cut2 ==  0 else arr2[cut2-1]
        #right side +inf
        right1 = sys.maxsize if cut1 == n else arr1[cut1]
        right2 = sys.maxsize if cut2 == m else arr2[cut2]
        
        #cross check mein agar cut valid hai toh left mein sabse bada
        if(left1<=right2 and left2 <= right1):
            return max(left1,left2)

        #upper wala bada hai toh search space kam karo
        elif(left1>right2):
            high = cut1 - 1
        #aur chota hai (left2>right1) then upper wala badhao
        else:
            low = cut1 + 1
            
            
    return 0 



a = [2,3,6,7,9]
b = [1,4,5,8,10]
k = 2
print(kthElement(a,b,len(a),len(b),k))