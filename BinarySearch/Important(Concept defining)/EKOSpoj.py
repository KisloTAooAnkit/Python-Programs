#https://www.spoj.com/problems/EKO/


def check(trees,target,bladeHeight):
    ans = 0
    for i in trees:
        res = i - bladeHeight
        ans += 0 if res < 0 else res 
    if(ans>=target):
        return True
    if(ans<target):
        return False


def soln(arr,target):

    ans = 0
    end = max(arr)
    start = 0
    while(start<=end):
        mid = start + (end-start)//2
        val = check(arr,target,mid)
        
        if(val):
            ans = mid
            start = mid+1
        elif(not val):
            end = mid-1
 

    return ans 

arr = [1 ,2 ,3 ,4 ,5 ,6, 7]
target = 8
print(soln(arr,target))