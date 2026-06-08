class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        record = {}
        res = []

        for i, v in enumerate(s):
            record[v] = i

        start = 0
        while start < len(s):
            char = s[start]
            idx = record[char]
            end = idx
            j = start
            while j < end:
                c = s[j]
                index = record[c]
                if index > end:
                    end = index
                j += 1
            res.append(s[start:end+1])
            start = end + 1
        
        return [len(word) for word in res]
        

