class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        
        for num in nums:
            res += [path + [num] for path in res if path + [num]  not in res]
        
        

        return res
