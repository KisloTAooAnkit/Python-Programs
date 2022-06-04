from collections import defaultdict, deque

#Tech dose soln confusing
def explorePathsDFS(graph,begin,endw,temp,ans):
    if begin == endw:
        temp.append(begin)
        ans.append(temp[:])
        temp.pop()
        return
    temp.append(begin)
    for nbr in graph[begin]:
        explorePathsDFS(graph,nbr,endw,temp,ans)
    temp.pop()
    return

def generateSpclGraphWithMinPath(begin,endW,wordList,spclGraph):
    wordList = set(wordList)
    s = "abcdefghijklmnopqrstuvwxyz"
    q = deque()
    levelMap = defaultdict(int)
    if endW not in wordList:
        return []
    levelMap[begin] = 1
    q.append((begin,1))
    while q:
        node,distance = q.popleft()
        for i in range(len(node)):
            for c in s:
                word = node[:i] + c + node[i+1:]
                
                if node[i] == c:
                    continue    

                if word in wordList:
                    if (word not in levelMap):
                        spclGraph[node].append(word)
                        levelMap[word] = distance +1
                        q.append((word,distance+1))
                    elif levelMap[word] == levelMap[node] + 1:
                        spclGraph[node].append(word)

def findLadders(begin,endW,wordList):
   spclGraph = defaultdict(list)
   generateSpclGraphWithMinPath(begin,endW,wordList,spclGraph)
   ans = []
   explorePathsDFS(spclGraph,begin,endW,[],ans)
   return ans


# MY solution
def sol(beginWord,endWord,wordList):
    q = deque()
    wordList = set(wordList)
    visited = defaultdict(int)
    graph = defaultdict(list)
    visited[beginWord] = 1
    q.append(beginWord)
    if endWord not in wordList:
        return []
    s = "abcdefghijklmnopqrstuvwxyz"
    while q:
        for i in range(len(q)):
            node = q.popleft()
            for i in range(len(node)):
                for c in s:
                    word = node[:i] + c + node[i+1:]
                    if word == node or word not in wordList:
                        continue
                    
                    if word not in visited:
                        q.append(word)
                        graph[node].append(word)
                        visited[word] = visited[node] + 1
                    
                    elif visited[word] == visited[node]+1:
                        graph[node].append(word)
    ans = []
    def dfs(b,e,temp,ans,g):
        if b == e:
            temp.append(b)
            ans.append(temp[:])
            temp.pop()
            return
        temp.append(b)
        for nbr in g[b]:
            dfs(nbr,e,temp,ans,g)
        temp.pop()
        return
    dfs(beginWord,endWord,[],ans,graph)
    return ans


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(sol(beginWord,endWord,wordList))


