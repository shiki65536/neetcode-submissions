from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        @cache
        def dfs(l, r):
            if l + 1 == r:
                return 0

            best = 0
            for i in range(l + 1, r):
                coins = nums[l] * nums[i] * nums[r]
                best = max(
                    best,
                    dfs(l, i) + coins + dfs(i, r)
                )

            return best

        return dfs(0, n - 1)
