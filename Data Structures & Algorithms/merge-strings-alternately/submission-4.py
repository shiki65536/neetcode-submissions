class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1 = i2 = 0
        l1, l2 = len(word1), len(word2)
        output = []

        while i1 < l1  and i2 < l2:
            output.append(word1[i1])
            output.append(word2[i2])
            i1 += 1
            i2 += 1
        
        if i1 < l1:
            for s in word1[i1:]:
                output.append(s)
        elif i2 < l2:
            for s in word2[i2:]:
                output.append(s)

        return "".join(output)
















        n, m = len(word1), len(word2)
        res = []

        for i in range(max(n, m)):
            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])

        return "".join(res)