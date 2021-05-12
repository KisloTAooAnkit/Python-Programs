""" find min health which is required to cross a grid without player dying (health going <=0) allowed dir : down and right """

import sys

def minHealth(hp,si,sj,ei,ej,grid,maxrow,maxcol):
    if(si==ei and sj == ej):
        return hp
    
    if(si>=maxrow or sj>=maxcol or si < 0 or sj < 0):
        return sys.maxsize
    
    hp += grid[si][sj]
    
    res1 = minHealth(hp,si+1,sj,ei,ej,maxrow,maxcol)
    res2 = minHealth(hp,si,sj+1,ei,ej,maxrow,maxcol)
    
    hp += min(res1,res2)
    if(hp<=0):
        return sys.maxsize
    else:
        return hp



def caller(grid):
    row = len(grid)
    col = len(grid[0])
    minHealth()


maze = [
        [2,-1,3],
        [4,-2,-4],
        [-10,8,-1]
        ]


