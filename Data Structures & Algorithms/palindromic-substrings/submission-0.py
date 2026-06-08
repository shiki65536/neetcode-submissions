class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []

        def expand(l, r):
            ans = []
            while 0 <= l and r < len(s) and s[l] == s[r]:
                ans.append(s[l:r+1])
                l -= 1
                r += 1
            return ans 
            
        

        for i in range(len(s)):
            odd_ans = expand(i, i)
            for pali in odd_ans:
                res.append(pali)

            even_ans =expand(i, i+1)
            for pali in even_ans:
                res.append(pali) 

        print(res)
        return len(res)
