class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total+nums[i]] += count
                dp[i+1][total-nums[i]] += count

        return dp[n][target]
        # count = 0
        # n = len(nums)

        # def backtrack(i: int, total: int) -> None:
        #     nonlocal count
        #     if i == n:
        #         if total == target:
        #             count += 1
        #         return

        #     backtrack(i + 1, total + nums[i])
        #     backtrack(i + 1, total - nums[i])

        # backtrack(0, 0)
        # return count