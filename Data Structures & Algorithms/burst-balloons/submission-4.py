class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = {}

        def dfs(l, r):
            if l + 1 == r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            best = 0
            for i in range(l + 1, r):
                coins = nums[l] * nums[i] * nums[r]
                best = max(
                    best,
                    dfs(l, i) + coins + dfs(i, r)
                )
            dp[l,r] = best
            return best

        return dfs(0, n - 1)
