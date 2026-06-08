class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def is_pali(l: int, r:int):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                return is_pali(left+1, right) or is_pali(left, right-1)
            left += 1
            right -= 1
        
        return True