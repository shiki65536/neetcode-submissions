class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        if N == 0:
            return ""

        def expand(start: int, end: int):
            while 0 <= start and end < len(s)  and s[start] == s[end]:
                start -= 1
                end += 1

            return (start+1, end-1)

        
        best_l, best_r = 0, 0

        for i in range(N):
            l1, r1 = expand(i, i)
            if r1 - l1 > best_r - best_l:
                best_l ,best_r = l1, r1

            l2, r2 = expand(i, i+1)
            if r2 - l2 > best_r - best_l:
                best_l, best_r = l2, r2
        
        return s[best_l:best_r + 1]