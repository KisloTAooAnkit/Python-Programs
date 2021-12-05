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
        
        
    def __searchWordHelper(self,root,word,n):
        
        if root.isTerminal:
            return True
        
        if n<0:
            return False
        
        idx = ord(word[n]) - 97
        child = None
        if root.children[idx]:
            child = root.children[idx]
        else:
            return False
        
        return self.__searchWordHelper(child,word,n-1)
    
    def searchWord(self,word,n):
        return self.__searchWordHelper(self.root,word,n)



class StreamChecker:


    def __fillTrie(self,word):
        self.trie.insertWord(word)

    def __init__(self, words):
        self.words = words
        self.trie = Trie()
        self.arr = []
        self.length = 0
        for word in words:
            self.__fillTrie(word[::-1])

    def query(self, letter: str) -> bool:
        self.arr.append(letter)
        self.length +=1
        return self.trie.searchWord(self.arr,self.length-1)