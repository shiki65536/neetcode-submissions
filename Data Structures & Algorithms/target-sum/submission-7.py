class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)

        def backtrack(i: int, total: int) -> None:
            nonlocal count
            if i == n:
                if total == target:
                    count += 1
                return

            backtrack(i + 1, total + nums[i])
            backtrack(i + 1, total - nums[i])

        backtrack(0, 0)
        return count