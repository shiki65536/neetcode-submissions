class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        need = [0] * 26
        win = [0] * 26

        for ch in s1:
            need[ord(ch) - ord("a")] += 1

        for r, ch in enumerate(s2):
            win[ord(ch) - ord("a")] += 1

            if r >= n:
                win[ord(s2[r - n]) - ord("a")] -= 1

            if win == need:
                return True

        return False
                        

