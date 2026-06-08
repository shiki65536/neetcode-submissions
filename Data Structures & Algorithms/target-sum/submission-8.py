class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)

        def dfs(i: int, total: int) -> int:
            if i == n:
                return 1 if total == target else 0

            key = (i, total)
            if key in memo:
                return memo[key]

            memo[key] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return memo[key]

        return dfs(0, 0)