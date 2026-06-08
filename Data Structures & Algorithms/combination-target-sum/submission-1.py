class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(start, remain):
            if remain == 0:
                res.append(subset[:])
                return
            if remain < 0:
                return
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i, remain - nums[i])
                subset.pop()
        
        backtrack(0, target)
        return res