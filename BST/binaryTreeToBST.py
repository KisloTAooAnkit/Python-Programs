def solution(arr,root,index):
    if not root or index[0]>=len(arr):
        return

    solution(arr,root.left,index)
    root.data = arr[index]
    index[0] +=1
    solution(arr,root.right,index)
    return