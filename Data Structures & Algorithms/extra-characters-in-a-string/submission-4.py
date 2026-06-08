class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]

            # option 1: treat s[i] as extra
            res = 1 + dfs(i + 1)

            # option 2: match any dictionary word
            for word in dictionary:
                right = i + len(word)
                if s[i:right] == word:
                    res = min(res, dfs(right))

            memo[i] = res
            return res

        return dfs(0)