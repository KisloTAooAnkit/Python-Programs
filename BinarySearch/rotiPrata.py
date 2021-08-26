import math
import sys
def equationroots(a,b,c): 
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
    if dis > 0: 
        
        root1 = (-b + sqrt_val)/(2 * a)
        root2 = (-b - sqrt_val)/(2 * a)
        return(max(int(root1),int(root2)))
      
    elif dis == 0: 
        
        root = (-b / (2 * a)) 
        return int(root)
    

def check(chefarr,currentTimeTarget,totalroti):
    possibleRotiCount = 0
   
    for chef in chefarr:
        c = -(currentTimeTarget*2) / chef
        a= 1
        b = 1
        possibleRotiCount+=equationroots(a,b,c)
    
    return possibleRotiCount >= totalroti
            
        


def rotiPrata(arr,target):
    n = max(arr)
    endTime = n*(target)*(target +1)/2
    startTime = 0
    ans =0
    while(startTime<=endTime):
        mid = startTime + (endTime-startTime)//2
        if(check(arr,mid,target)):
            ans = mid
            endTime = mid-1
        else:
            startTime = mid+1
    return ans        

test = int(input())
while(test):
    roticount = int(input())
    arr = list(map(int,input().strip().split()))
    print(rotiPrata(arr[1:],roticount))
    test-=1


