"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
https://leetcode.com/problems/shuffle-the-array/    
"""

#O(N) with extra space O(N)
def shuffle(nums,n) :
    temp = []
    i =0
    j=n
    while(i<n and j < 2*n):
        temp.append(nums[i])
        temp.append(nums[j])
        i+=1
        j+=1
    return temp

#O(N) beautiful solution with no extraSpace https://leetcode.com/problems/shuffle-the-array/discuss/675956/In-Place-O(n)-Time-O(1)-Space-With-Explanation-and-Analysis

def suffleCoolerOne(arr,n):
    i = n-1
    j = 2*n-1

    while(i>=0):
        arr[j] = arr[j]<<10
        arr[j] = arr[j] | arr[i]
        j-=1
        i-=1
    
    i=0
    j=n
    while(j<2*n):
        num1 = arr[j] & 1023
        num2 = arr[j] >> 10 
        arr[i] = num1
        arr[i+1] = num2
        i+=2
        j+=1
    
    return arr


arr = [2,5,1,3,4,7]
n=3

print(suffleCoolerOne(arr,n))

        
    