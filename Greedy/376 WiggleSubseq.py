
def wiggleGreedy(arr):
    length = 1
    increasing = None
    n = len(arr)
    for i in range(1,n):

        if arr[i-1] < arr[i] and increasing != True:
            increasing = True
            length +=1
        elif arr[i-1] > arr[i] and increasing != False:
            increasing = False
            length +=1
    return length

