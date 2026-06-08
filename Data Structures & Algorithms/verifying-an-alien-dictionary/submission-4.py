class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = max(len(word) for word in words)
        order = {c:i for i, c in enumerate(order)}

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if len(words[i+1]) <= j:
                    return False
                if order[words[i][j]] < order[words[i+1][j]]:
                    break
                if order[words[i][j]] > order[words[i+1][j]]:
                    return False   
        return True
                    