class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(remain):
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            if remain in memo:
                return memo[remain]

            total = 0
            for num in nums:
                total += dfs(remain - num)

            memo[remain] = total
            return total
        return dfs(target)

