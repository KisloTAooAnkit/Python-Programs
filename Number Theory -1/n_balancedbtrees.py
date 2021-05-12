
#given a height h find number of balanced b trees variations possible 
#balanced b tree at for a root node = | lh - rh | <= 1

def findHeight(h):
    if h == 0 or h == 1:
        return 1 
    #ans = (findHeight(h-1)*findHeight(h-1)) + 2 * (findHeight(h-1)*findHeight(h-2))
    x = findHeight(h-1)
    y = findHeight(h-2)
    ans = x*x + 2*x*y
    return ans

#
#for evernode to be balanced possible cases are 

#     (h)             (h)            (h)
#    /   \           /   \        /      \
#(h-1)   (h-1)   (h-1)   (h-2)  (h-2)   (h-1)
   
print(findHeight(10))
