class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return [""]

            res = []

            for j in range(i, len(s)):
                word = s[i:j + 1]

                if word in words:
                    tails = dfs(j + 1)

                    for tail in tails:
                        if tail:
                            res.append(word + " " + tail)
                        else:
                            res.append(word)

            memo[i] = res
            return res

        return dfs(0)