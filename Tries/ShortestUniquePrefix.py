class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.isEnd = False
        self.unqWordsThruMe = 1
        self.children = [None]*26

class Trie:
    def __init__(self) -> None:
        self.root = Node("")
    

    def __insert(self,root,word):
        if len(word) == 0:
            root.isEnd = True
            return
        
        idx = ord(word[0]) - 97
        child = None
        if root.children[idx]:
            child = root.children[idx]
            child.unqWordsThruMe +=1
        else:
            child = Node(word[0])
            root.children[idx] = child
        
        self.__insert(child,word[1:])
        return

    def insert(self,word):
        self.__insert(self.root,word)

    def __findPrefix(self,root,word):
        if len(word) == 0:
            return ""
        
        idx = ord(word[0]) - 97
        if root.children[idx].unqWordsThruMe > 1:
            return word[0] + self.__findPrefix(root.children[idx],word[1:])
        else:
            return word[0]


    def findUniquePrefix(self,word):
        return self.__findPrefix(self.root,word)


arr = ["geeksgeeks", "geeksquiz", "geeksforgeeks"]
trie = Trie()
for i in arr:
    trie.insert(i)

ans = []
for i in (arr):
    val = trie.findUniquePrefix(i)
    ans.append(val)
print(ans)