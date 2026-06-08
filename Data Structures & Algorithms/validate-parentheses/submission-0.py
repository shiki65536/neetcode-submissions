class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"}": "{", "]": "[", ")": "("}
        stack = []

        for c in s:
            if c in pair:
                if not stack:
                    return False
                if pair[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return True if not stack else False