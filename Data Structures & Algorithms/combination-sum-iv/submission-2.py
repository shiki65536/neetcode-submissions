class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target+1)
        dp[0] = 1 # one method

        #dp[i] = dp[i-coin]

        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]

        return dp[-1]
        # dfs + memo
        # memo = {}

        # def dfs(remain):
        #     if remain == 0:
        #         return 1
        #     if remain < 0:
        #         return 0
        #     if remain in memo:
        #         return memo[remain]

        #     total = 0
        #     for num in nums:
        #         total += dfs(remain - num)

        #     memo[remain] = total
        #     return total
        # return dfs(target)

