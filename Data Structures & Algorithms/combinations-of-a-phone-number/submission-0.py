class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(start, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            for i in range(start, len(digits)):
                ch = digits[i]
                for c in digitToChar[ch]:
                    path.append(c)
                    backtrack(i+1, path)
                    path.pop()
        
        backtrack(0, [])
        return res

