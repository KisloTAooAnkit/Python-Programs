


def getRightMostNode(node,curr):
    #we only search in extreme right subtrees
    while(node.right and node.right != curr):
        node = node.right
    return node


def MorrisInOrderTraversal(node):
    ans = []
    curr = node

    while(curr):
        leftPtr = node.left
        #if left subtree dosent exist print node
        if not leftPtr:
            ans.append(curr.val)
            curr = curr.right
        #if subtree exists
        else:
            #get the rightmost node (non null)
            rightMostNode = getRightMostNode(leftPtr,curr)
            #if rightmost node right pointer is null then we create a thread to curr(parent)
            #and curr goes in left subtree
            if not rightMostNode.right:
                rightMostNode.right = curr
                curr = curr.left

            #if rightmost node right pointer has some value that means thread is already created 
            # hence for current node left subtree is explored
            # break the thread and print curr and then move to curr to right subtree
            else:
                rightMostNode.right = None
                ans.append(curr.val)
                curr = curr.right
    return ans

