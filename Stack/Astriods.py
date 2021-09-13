#https://leetcode.com/problems/asteroid-collision/
def solnHelper(arr):
    count = 0
    stack =[]
    n = len(arr)
    for i in range(n):

    
        abs1 = abs(arr[i])
        continueFlag = False
        while(count>0 and ((arr[i]//(abs1)) != (stack[-1]//abs(stack[-1])))):
            if(stack[-1]>-1 and arr[i]<0):
                if(abs1 > abs(stack[-1])):
                    stack.pop(-1)
                    count-=1
                elif(abs1<abs(stack[-1])):
                    continueFlag = True
                    break
                
                elif(abs1 == abs(stack[-1])):
                    count-=1
                    stack.pop(-1)
                    continueFlag = True
                    break
            else:
                break
            

        if not continueFlag:
            stack.append(arr[i])
            count +=1
    return stack

a = [-2,-1,1,-2]
print(solnHelper(a))            

