class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        memo = {}
        def dfs(i):
            if i == N:
                return True
            if i in memo:
                return memo[i]
            for word in wordDict:
                j = len(word)
                if s[i:i+j] == word:
                    if dfs(i+j):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)

        
        
        
        
        
        
        
        
        
        
        # wordSet = set(wordDict)
        # memo = {len(s): True}








        
        # wordSet = set(wordDict)
        # memo = {len(s): True}

        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
            
        #     for j in range(i, len(s)):
        #         if s[i: j+1] in wordSet and dfs(j+1):
        #             memo[i] = True
        #             return True
        #     memo[i] = False
        #     return False

        # return dfs(0)