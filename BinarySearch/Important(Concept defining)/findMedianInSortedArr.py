"""since we want to find median we need to divide merged sorted array from middle and then consider middle element 
        we want to implement d same thinking but wihtout mergeing two arrays hence we try to find proper cut 
        via bin search"""

import sys
def findMedianSortedArr(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    #always work on smaller array for less complexity in binsearch
    if(n2<n1):
        return findMedianSortedArr(arr2,arr1)
    
    low = 0 
    high = n1
    while(low<=high):
        #find the cut in arr1 cut = number of elements before cut
        cut1 = low + (high-low)//2
        #collect remaining elements from arr2 for statisfying number of elements in first half of merged arr

        cut2 = (n1+n2)//2 - cut1

        """identifying if the cuts are valid -> agar ham cuts ke left sides ko merge kare aur ight side ko merge kar
        to continous sorted array milni chahiye"""

        """Now how to check if the cuts are valid wihtout merging ?"""
        
        """pick last two elements from left sides of cuts left1,left2"""
        
        left1 = -sys.maxsize if cut1 ==0 else arr1[cut1-1]
        left2 = -sys.maxsize if cut2 ==0 else arr1[cut2-1]
        
        """pick first two elements from right side of cuts right1,right2"""
        
        right1 = sys.maxsize if cut1 == n1 else arr1[cut1]
        right2 = sys.maxsize if cut2 == n2 else arr2[cut2]

        """Niche wala logic kyun work karta hai uske liye khud example lo aur dry run karo samjhega"""
        
        """cross compare left and right sides of cut if anyone is invalid then we decide its a bad cut nahi toh 
        ham accept karte hai ki sahi cut hai and we can calculate median"""

        if(left1 <= right2 and left2<=right1):
            """cut is valid"""
            if((n1+n2)%2==0):
                """even length pe beech ke do elements ka half hota hai median"""
                return (max(left1,left2)+min(right1,right2))/2
            else:
                """odd lenght ke liye middle ele hota hai median"""
                return (max(left1,left2))

        else:
            """if cut was invalid adjust new searching space by adjusting high and low"""
            if(left1>right2):
                """is case mein hame left1 ko reduce karna hoga valid cut banane ke liye hence we shift partition of arr1 
                to the lft side"""
                high = cut1 -1
            else:
                """is case mein hamara partition ko right side bhejte hai  """
                low = cut1 + 1
        
    return 0


