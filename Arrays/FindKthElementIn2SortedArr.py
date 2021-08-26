def kthElement(arr1,arr2,k):
    n1 = (len(arr1))
    n2 = len(arr2)
    piv1=0
    piv2 = 0
    count =0
    if(k>n1+n2):
        return -1
    if(k==0):
        return min(arr1[0],arr2[0])
    while(piv1<n1 and piv2<n2):
        if(arr1[piv1]<=arr2[piv2]):
            count+=1
            if(count==k):
                return arr1[piv1]
            piv1 +=1
            
        elif(arr1[piv1]>arr2[piv2]):
            count+=1
            if(count==k):
                return arr2[piv2]
            piv2+=1

    while(piv1<n1):
        count+=1
        if(count==k):
            return arr1[piv1]
        piv1+=1
    
    while(piv2<n2):
        count+=1
        if(count==k):
            return arr2[piv2]
        piv2+=1

a = [100]
b = [72]
k=2
print(kthElement(a,b,k))