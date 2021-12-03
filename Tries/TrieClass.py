class TrieNode :
    def __init__(self,data) -> None:
        self.data = data
        self.children = [None]*26
        self.isTerminal = False
    
class Trie:
    def __init__(self) -> None:
        self.root  = TrieNode("")

    def __insertWordHelper(self,root,word):
        if len(word) == 0:
            root.isTerminal = True
            return
        idx = ord(word[0]) - 97
        child = None
        if root.children[idx]:
            child = root.children[idx]
        else:
            child = TrieNode(word[0])
            root.children[idx] = child
        
        self.__insertWordHelper(child,word[1:])
        
    def insertWord(self,word):
        self.__insertWordHelper(self.root,word)
        
        
    def __searchWordHelper(self,root,word):
            
        if len(word) == 0:
            if not root.isTerminal:
                return False
            return True
        
        idx = ord(word[0]) - 97
        child = None
        if root.children[idx]:
            child = root.children[idx]
        else:
            return False
        
        return self.__searchWordHelper(child,word[1:])
    
    def searchWord(self,word):
        return self.__searchWordHelper(self.root,word)


trie = Trie()
trie.insertWord("abc")
trie.insertWord("abd")
trie.insertWord("abe")
print(trie.searchWord("ab"))