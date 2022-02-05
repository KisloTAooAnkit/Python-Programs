

class TrieNode:
    def __init__(self,data) -> None:
        self.data = data
        self.children = [None]*26
        self.isTerminal = False



class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("")

    def insertWord(self,word):
        self.__insertWordHelper(self.root,word)

    def __insertWordHelper(self,root,word):
        if len(word) == 0:
            root.isTerminal = True
            return
        
        idx = -1
        
        idx = ord(word[0]) - 97

        child = None
        if root.children[idx]:
            child = root.children[idx]
        else:
            child = TrieNode(word[0])
            root.children[idx] = child
        
        self.__insertWordHelper(child,word[1:])
        return


    def searchWord(self,word) -> bool :
        return self.__searchWordHelper(self.root,word)

    def __searchWordHelper(self,root,word):
        if len(word) == 0:
            return root.isTerminal
        ans = False
        if word[0] == ".":
            for i in range(26):
                if root.children[i]:
                    ans = ans or self.__searchWordHelper(root.children[i],word[1:])

                    if ans:
                        return True
            return ans
        
        idx = ord(word[0]) - 97

        if root.children[idx]:
            return self.__searchWordHelper(root.children[idx],word[1:])
        else:
            return False



command = ["WordDictionary","addWord","addWord","search","search","search","search","search","search","search","search"]

data = [[],["a"],["ab"],["a"],["a."],["ab"],[".a"],[".b"],["ab."],["."],[".."]]
trie = None
for i,val in enumerate(command):
    if val == "WordDictionary":
        trie = Trie()
    elif val == "addWord":
        trie.insertWord(data[i][0])
    elif val == "search":
        print(trie.searchWord(data[i][0]))



