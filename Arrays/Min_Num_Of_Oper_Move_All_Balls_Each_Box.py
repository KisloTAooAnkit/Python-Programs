def minOperations(boxes):
    n= len(boxes)
    leftsum = [0]*n
    rightsum = [0]*n
    ans = [0]*n
    ans1 = [0]*n
    for i in range(n-2,-1,-1):
        factor = 0
        if(boxes[i+1]=="1"):
            factor = 1
        
        rightsum[i] = rightsum[i+1] + factor
    

    for i in range(1,n):
        factor =0
        if(boxes[i-1]=="1"):
            factor = 1
        
        leftsum[i] = leftsum[i-1] + factor


    for i in range(n-2,-1,-1):
        ans[i] += rightsum[i] + ans[i+1]

    
    for j in range(1,n):
        ans1[j] += leftsum[j] + ans1[j-1]
    
    return [ans1[i] + ans[i] for i in range(0,n) ]


        







boxes = "0010101"

print(minOperations(boxes))

