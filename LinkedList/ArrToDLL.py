class Node:
     
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
 
# Utility function to create a node in memory
def getNode():
 
    return (Node(0))
 
# Function to display the list
def displayList(temp):
 
    t = temp
    if(temp == None):
        return 0
    else:
         
        print("The list is: ", end = " ")
         
        while(temp.next != t):
         
            print(temp.data, end = " ")
            temp = temp.next
         
        print(temp.data)
         
        return 1
     
# Function to convert array into list
def createList(arr, n, start):
 
    # Declare newNode and temporary pointer
    newNode = None
    temp = None
    i = 0
     
    # Iterate the loop until array length
    while(i < n):
     
        # Create new node
        newNode = getNode()
         
        # Assign the array data
        newNode.data = arr[i]
         
        # If it is first element
        # Put that node prev and next as start
        # as it is circular
        if(i == 0):
         
            start = newNode
            newNode.prev = None
            newNode.next = None
         
        else:
             
            # Find the last node
            temp = (start).prev
             
            # Add the last node to make them
            # in circular fashion
            temp.next = newNode
            newNode.next = start
            newNode.prev = temp
            temp = start
            temp.prev = newNode
        i = i + 1
    return start