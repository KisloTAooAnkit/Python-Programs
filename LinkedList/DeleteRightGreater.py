#https://practice.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1
def deleteRight(head):
    if not head.next:
        return head

    
    node = deleteRight(head.next)
    if node.data > head.data:
        return node
    else:
        head.next = node
    return head
