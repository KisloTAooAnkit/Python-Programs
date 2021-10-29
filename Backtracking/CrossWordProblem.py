n = 10

def canWePlaceVertically(matrix,word,row,col,wordlen):
    for i in range(wordlen):
        if matrix[i+row][col] == word[i] or matrix[i+row][col] == "-":
            wordlen -=1
    return wordlen == 0

def canWePlaceHorizontally(matrix,word,row,col,wordlen):
    for i in range(wordlen):
        if matrix[row][i+col] == word[i] or matrix[row][i+col] == "-":
            wordlen -=1
    return wordlen == 0

def placeVertically(matrix,word,row,col,checkArr,wordlen):
    for i in range(wordlen):
        if matrix[row + i][col] == word[i]:
            continue
        matrix[i+row][col] = word[i]
        checkArr[i] = True

def placeHorizontally(matrix,word,row,col,checkArr,wordlen):
    for i in range(wordlen):
        if matrix[row][col+i] == word[i]:
            continue
        matrix[row][col+i] = word[i]
        checkArr[i] = True
        
def removeHorizontally(matrix,row,col,checkArr,wordlen):
    for i in range(wordlen):
        if checkArr[i]:
            matrix[row][col+i] = "-"
    
def removeVertically(matrix,row,col,checkArr,wordlen):
    for i in range(wordlen):
        if checkArr[i]:
            matrix[row+i][col] = "-"
    

def crossword(matrix,arr,idx):
    if idx >= len(arr):
        return True

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "-" or matrix[i][j] == arr[idx][0]:
                wordlen = len(arr[idx])
                if canWePlaceVertically(matrix,arr[idx],i,j,wordlen):
                    checkArr = [False]*wordlen
                    placeVertically(matrix,arr[idx],i,j,checkArr,wordlen)
                    if crossword(matrix,arr,idx+1):
                        return True
                    removeVertically(matrix,i,j,checkArr,wordlen)
            
                    
                if canWePlaceHorizontally(matrix,arr[idx],i,j,wordlen):
                    checkArr = [False]*wordlen
                    placeHorizontally(matrix,arr[idx],i,j,checkArr,wordlen)
                    if crossword(matrix,arr,idx+1):
                        return True
                    removeHorizontally(matrix,i,j,checkArr,wordlen)
    return False

[
    ["+","-","+","+","+","+","+","+","+","+"],
    ["+","-","+","-","+","+","+","+","+","+"],
    ["+","-","-","-","-","-","-","-","+","+"],
    ["+","-","-","+","+","-","+","+","+","+"],
    ["+","-","+","+","+","-","+","+","+","+"],
    ["+","-","+","+","+","+","+","+","+","+"],
    ["+","-","+","+","+","+","+","+","+","+"],
    ["+","-","+","+","+","+","+","+","+","+"],
    ["+","-","+","+","+","+","+","+","+","+"],
    ["+","-","+","+","+","+","+","+","+","+"],
    
 ]