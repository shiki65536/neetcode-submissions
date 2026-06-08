class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        n1, n2 = len(word1), len(word2) 
        l = 0

        while l < n1 and l < n2:
            result.append(word1[l])
            result.append(word2[l])
            l += 1
        
        output = "".join(result)
        
        output += word1[l:] + word2[l:]

        return output