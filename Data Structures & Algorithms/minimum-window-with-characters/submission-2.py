class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n < m or m == 0:
            return ""
        need, win = {}, {}
        res, res_len = [-1, -1], float("inf")
        for c in t:
            need[c] = need.get(c, 0) + 1 

        count = len(need)
        l = 0
        have = 0

        for r in range(n):
            char = s[r]
            win[char] = win.get(char, 0) + 1
            if char in need and win[char] == need[char]:
                have += 1
                while have == count:
                    if r-l+1 < res_len:
                        res = [l, r]
                        res_len = r-l+1
                    ch = s[l]
                    win[ch] -= 1
                    if ch in need and win[ch] < need[ch]:
                        have -= 1
                    l += 1
                
        return s[res[0]:res[1]+1]
