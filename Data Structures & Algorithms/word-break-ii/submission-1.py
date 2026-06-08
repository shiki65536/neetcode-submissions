class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output = []

        def backtrack(i, sentence):
            if i == len(s):
                answer = " ".join(sentence)
                output.append(answer)
                return
            if i > len(s):
                return
            
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in wordDict:
                    sentence.append(word)
                    backtrack(j+1, sentence)
                    sentence.pop()
        backtrack(0, [])
        return output
















        wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur))
                return

            for j in range(i, len(s)):
                w = s[i:j + 1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j + 1)
                    cur.pop()

        cur = []
        res = []
        backtrack(0)
        return res