class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        adj = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj[pattern].append(word)

        queue = deque([beginWord])

        visited = set(beginWord)
        res = 1
        while queue:
            for _ in range(len(queue)): 
                word = queue.popleft()
                if word == endWord:
                    return res     

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:] 
                    for nei in adj[pattern]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(word)  
            res+=1
             
        return 0
