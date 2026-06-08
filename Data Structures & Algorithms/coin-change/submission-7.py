class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("INF")] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin]+1, dp[i])

        return dp[-1] if dp[-1] != float("INF") else -1


















        # INF = amount + 1
        # dp = [INF] * (amount + 1)
        # dp[0] = 0

        # for a in range(1, amount + 1):
        #     for c in coins:
        #         if a - c >= 0:
        #             dp[a] = min(dp[a], dp[a - c] + 1)

        # return -1 if dp[amount] == INF else dp[amount]