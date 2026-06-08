class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def expand(l, r):
            cnt = 0
            while 0 <= l and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt 
            
        

        for i in range(len(s)):
            res += expand(i, i)

            res += expand(i, i+1)



        return res
