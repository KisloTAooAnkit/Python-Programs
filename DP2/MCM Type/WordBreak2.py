class Solution:
    def wordBreak(self, s: str, wordDict):
        
        #making set for O(1) lookup
        wordDict = set(wordDict)

        #memo for pruning recursive calls
        memo = {}
        

        def helper(sub):
            #DP
            if sub in memo:
                return memo[sub]
            
            res = []
            for i in range(len(sub)):
                prefix = sub[:i+1]
                #if its a valid prefix
                if prefix in wordDict:
                    
                    #early return if the partition is whole input string itself
                    if prefix == sub:
                        res.append(prefix)
                    

                    else:
                        #get list of suffixes
                        suffixes = helper(sub[i+1:])
                        #for every suffixes we append current prefix
                        for suffix in suffixes:
                            suffixTillNow = prefix + " " + suffix
                            res.append(suffixTillNow)
            #we memoized the current list
            memo[sub] = res
            # we return list of strings then as suffix
            return res

        
        return helper(s)