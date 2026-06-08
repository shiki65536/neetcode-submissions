class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        wordList.append(beginWord)
        patterns = {}
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern not in patterns:
                    patterns[pattern] = []
                patterns[pattern].append(word)
        
        queue = deque([beginWord])
        visited =  {beginWord}
        res = 0

        while queue:
            size = len(queue)
            res += 1
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in patterns[pattern]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
        
        return 0




