class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, remain, path):
            if remain == 0:
                result.append(path[:])
                return
            if remain < 0:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, remain - nums[i], path)  # i (允許重複使用)
                path.pop()

        backtrack(0, target, [])
        return result