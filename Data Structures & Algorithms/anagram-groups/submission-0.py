class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for string in strs:
            key = "".join(sorted(string))
            if key not in hash_table:
                hash_table[key] = []
            hash_table[key].append(string)

        return list(hash_table.values())
