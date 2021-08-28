def findSubarrays(arr):
    runningsum =0
    n = len(arr)
    dic = dict()
    for i in range(n):
        val = arr[i]
        if(val not in dic):
            val = []
            pass    