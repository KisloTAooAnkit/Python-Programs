#https://practice.geeksforgeeks.org/problems/arithmetic-number2815/1#
def inSequence(A, B, C):

        # code here
    if(C==0):
        if(A==B):
            return 1
        else:
            return 0
    diff = B-A
    if(diff%C==0 and diff//C >=0):
        return 1
    else:
        return 0