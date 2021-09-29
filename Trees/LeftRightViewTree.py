from queue import SimpleQueue
class HorizontalViewsOfATree:
    
    def helper_Right_DFS(self,root,arr,level):
        if not root:
            return
        if level == len(arr):
            arr.append(root.val)

        self.helper_Right_DFS(root.right,arr,level+1)
        self.helper_Right_DFS(root.left,arr,level+1)

#"""---------------------------------------------------------------------------------------------------"""
    def helper_Left_DFS(self,root,arr,level):
        if not root:
            return
        if level == len(arr):
            arr.append(root.val)

        self.helper_Left_DFS(root.left,arr,level+1)
        self.helper_Left_DFS(root.right,arr,level+1)

#"""---------------------------------------------------------------------------------------------------"""

    def BFS_Left_View(self,root,arr):
        q = SimpleQueue()
        q.put(root)
        q.put(None)
        flagToInsert = True
        count = 2
        while count>1 :
            node = q.get()
            count -=1
            if node != None:
                if flagToInsert:
                    arr.append(node.val)
                    flagToInsert = not flagToInsert

                if node.left:
                    q.put(node.left)
                    count+=1
                if node.right:
                    q.put(node.right)
                    count+=1
            else:
                q.put(None)
                count+=1
                flagToInsert = True
        return arr
#"""---------------------------------------------------------------------------------------------------"""

    def BFS_Right_View(self,root,arr):
        q = SimpleQueue()
        q.put(root)
        q.put(None)
        flagToInsert = True
        count = 2
        while count>1 :
            node = q.get()
            count -=1
            if node != None:
                if flagToInsert:
                    arr.append(node.val)
                    flagToInsert = not flagToInsert

                if node.right:
                    q.put(node.right)
                    count+=1
                if node.left:
                    q.put(node.left)
                    count+=1
            else:
                q.put(None)
                count+=1
                flagToInsert = True
        return arr
        
        