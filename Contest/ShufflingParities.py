def soln(arr,n):
    oddcount = 0
    evencount = 0
    evenplaces = 0
    oddplaces = 0
    if(n%2==0):
        evenplaces = oddplaces = n//2
    else:
        oddplaces = (n//2) + 1
        evenplaces = n-oddplaces

    for i in arr:
        if(i%2==0):
            evencount +=1
        else:
            oddcount +=1

    a = min(oddcount,evenplaces)
    b = min(evencount,oddplaces)
    return a+b
    
