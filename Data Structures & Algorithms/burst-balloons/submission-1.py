class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = {}

        def dfs(l, r):
            # open interval (l, r), no balloons left inside = 0
            if r - l < 2:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            best = 0
            for i in range(l + 1, r):  # i is the LAST balloon to burst in (l,r)
                coins = nums[l] * nums[i] * nums[r]
                rest = dfs(l, i) + dfs(i, r)
                best = max(best, coins + rest)

            dp[(l, r)] = best
            return best

        return dfs(0, n - 1)
