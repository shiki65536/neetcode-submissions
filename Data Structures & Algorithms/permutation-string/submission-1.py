class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        ref = [0]*26
        window = [0]*26

        for i in range(n1):
            d1 = ord(s1[i]) - ord("a")
            d2 = ord(s2[i]) - ord("a")
            ref[d1] += 1
            window[d2] += 1
        
        if ref == window:
            return True

        for r in range(n1, n2):
            l = r - n1
            d_r = ord(s2[r]) - ord("a")
            d_l = ord(s2[l]) - ord("a")
            window[d_r] += 1
            window[d_l] -= 1
            if ref == window:
                return True
        
        return False













        # n, m = len(s1), len(s2)
        # if n > m:
        #     return False

        # need = [0] * 26
        # win = [0] * 26

        # for ch in s1:
        #     need[ord(ch) - ord("a")] += 1

        # for r, ch in enumerate(s2):
        #     win[ord(ch) - ord("a")] += 1

        #     if r >= n:
        #         win[ord(s2[r - n]) - ord("a")] -= 1

        #     if win == need:
        #         return True

        # return False
                        

