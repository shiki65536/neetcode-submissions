class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
    
        memo = {} #(i, j) = word
        output = []
        path = []

        def backtrack(i):
            if i == n:
                output.append(path[:])
                return
            for j in range(i, n):
                word = s[i:j+1] 
                if word == word[::-1]:
                    path.append(word)
                    backtrack(j+1)
                    path.pop()
        
        
        backtrack(0)
        return output















        # res = []
        # path = []

        # def isPali(l, r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True

        # def backtrack(start):
        #     if start == len(s):
        #         res.append(path[:])
        #         return
        #     for i in range(start, len(s)):
        #         if isPali(start, i):
        #             path.append(s[start:i+1])
        #             backtrack(i+1)
        #             path.pop()
        
        # backtrack(0)
        # return res
