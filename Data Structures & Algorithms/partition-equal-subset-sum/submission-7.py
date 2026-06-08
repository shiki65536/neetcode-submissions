from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}

        def dfs(i: int, remain: int) -> bool:
            if remain == 0:
                return True
            if remain < 0 or i == len(nums):
                return False
            key = (i, remain)
            if key in memo:
                return memo[key]

            # choose nums[i] or skip it
            memo[key] = dfs(i + 1, remain - nums[i]) or dfs(i + 1, remain)
            return memo[key]

        return dfs(0, target)