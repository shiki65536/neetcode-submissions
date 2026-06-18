class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                del_l = is_palindrome(l+1, r)
                del_r = is_palindrome(l, r-1)
                return del_l or del_r
        
        return True


















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