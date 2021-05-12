# Brute Force Approach using prefix sum complexity O(n^4)
def maxSumRectPrefixSum(rect):
    
    row = len(rect)
    col = len(rect[0])
    sumrect = [[0 for i in range(col)] for j in range(row)]
    
    currsum =0
    maxsum = 0
    
    cd1,cd4 = 0,0
    
    for i in range(row):
        for j in range(col):
            sumrect[i][j] = fillSum(i,j,rect)  
    
    for i in range(row):
        for j in range(col):
            first = (i,j)
            
            for row2 in range(i,row):
                second = (row2,j)
                
                for col2 in range(j,col):
                    third = (i,col2)
                    
                    fourth = (row2,col2)
                    
                    currsum = calcSum(first,second,third,fourth,sumrect)
                                        
                    if currsum>maxsum:
                        cd1 = first
                        cd4 = fourth
                        maxsum = currsum          
                        
    return maxsum , cd1, cd4
                
def fillSum(x,y,rect):
    ans =0
    for i in range(x,len(rect)):
        for j in range(y,len(rect[0])):
          ans+=rect[i][j]
    return ans  

def calcSum(first,second,third,fourth,sumrect):
    row = len(sumrect)
    col = len(sumrect[0])
    
    fstsum,secsum,thrdsum,frthsum = 0,0,0,0
    
    fstsum = sumrect[first[0]][first[1]]
    
    secsum = 0 if (second[0]+1) == row else sumrect[second[0]+1][second[1]] 

    thrdsum = 0 if (third[1]+1) == col else sumrect[third[0]][third[1]+1]
    
    frthsum = 0 if ((fourth[0]+1) == row or (fourth[1] +1) == col) else sumrect[fourth[0]+1][fourth[1]+1] 
    
    ans = fstsum - secsum - thrdsum + frthsum
        
    return ans
#########################################################  
    
    

    
    
M = [
     [1, 2, -1],
     [-8, -3, 4],
     [3, 8, 10]  
     ]

M1 = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]

print(maxSumRectPrefixSum(M1))

