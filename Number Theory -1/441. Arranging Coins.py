import math
def arrangeCoins(sumOfTerms):
    d = math.sqrt(1 + (4*1*2*sumOfTerms))
    root = (-1 + d)/2
    return root

n = 10
print(arrangeCoins(n))