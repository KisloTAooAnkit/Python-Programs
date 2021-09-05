
class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
 
# Function to insert Node
def insert(root, item):
    temp = Node(0)
    temp.data = item
    temp.next = root
    root = temp
    return root
 
def display(root):
    while (root != None):
        print(root.data, end=" ")
        root = root.next
 
def arrayToList(arr, n):
    root = None
    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])
    return root
