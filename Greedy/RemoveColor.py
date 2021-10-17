def winnerOfGame(colors):
    a = 0
    b = 0
    n = len(colors)
    for i in range(1,n-1):
        if colors[i] == "A":
            if colors[i-1] == colors[i] == colors[i+1]:
                a+=1
        else:
            if colors[i-1] == colors[i] == colors[i+1]:
                b+=1
    return a>b
            