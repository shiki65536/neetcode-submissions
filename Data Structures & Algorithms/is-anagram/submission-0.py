class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # error 
        if not isinstance(s, str) or not isinstance(t, str):
            raise TypeError("s and t must be strings")
        return Counter(s) == Counter(t)


# dry run
## isAnagram(0, 1)
