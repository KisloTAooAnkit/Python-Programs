#https://leetcode.com/problems/trapping-rain-water/

def trap(height):
    n = len(height)
    
    if(n<3):
        return 0
    
    leftGreatestHeights=[0]*n
    rightGreatestHeights = [0]*n
    ans = 0
    
    leftGreatestHeights[0] = height[0]
    rightGreatestHeights[-1] = height[-1]
    
    #left sweep
    for i in range(1,n-1):
        if(leftGreatestHeights[i-1]>height[i]):
            leftGreatestHeights[i] = leftGreatestHeights[i-1]
        else:
            leftGreatestHeights[i] = height[i]
    
    for i in range(n-2,0,-1):
        if(height[i]<rightGreatestHeights[i+1]):
            rightGreatestHeights[i] = rightGreatestHeights[i+1]
        else:
            rightGreatestHeights[i] = height[i]
    
    for i in range(1,n-1):
        ans = ans + min(leftGreatestHeights[i],rightGreatestHeights[i]) - height[i]
        
    
    print(leftGreatestHeights)
    print(rightGreatestHeights)
    print(ans)
    
height = [4,2,4]


trap(height)
    