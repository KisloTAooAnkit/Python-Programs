import Trees.BuildTreeFromStr 
def printElementsInRange(root,start,end,arr):
    if not root:
        return 
    
    if start <= root.data <= end:
        printElementsInRange(root.left,start,end)
        arr.append(root.data)
        printElementsInRange(root.right,start,end)
    
    elif root.data < start:
        printElementsInRange(root.right,start,end)
    else:
        printElementsInRange(root.left,start,end)

    return

arr = [8, 5 ,10 ,2 ,6 ,"null","null","null", "null", "null", 7 ,"null","null"]
root = Trees.BuildTreeFromStr.buildTree(arr)
start = 6
end = 10
printElementsInRange(root,start,end)
