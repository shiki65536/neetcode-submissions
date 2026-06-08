class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        prefix = ""

        for i in range(min_len):
            tmp = strs[0][:i+1]
            for s in strs:
                if s[:i+1] != tmp:
                    return prefix
            prefix = tmp
        
        return prefix