#https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/


def maxWidthOfVerticalArea(points):
    points.sort()
    maxwidth =0
    n = len(points)
    for i in range(1,n):
        maxwidth = max(
            maxwidth,
            points[i][0] - points[i-1][0]
            )
    return maxwidth
  


a= [[8,7],[9,9],[7,4],[9,7]]
print(maxWidthOfVerticalArea(a))