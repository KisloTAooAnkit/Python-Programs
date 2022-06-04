def populateNextRecur(root, next_ref):
 
    if (root != None):
 
        # First set the next pointer in right subtree
        populateNextRecur(root.right, next_ref)
 
        # Set the next as previously visited node in reverse Inorder
        root.next = next_ref
 
        # Change the prev for subsequent node
        next_ref = root
 
        # Finally, set the next pointer in right subtree
        populateNextRecur(root.left, next_ref)