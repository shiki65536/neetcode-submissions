class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0

        dp = [0] * n
        dp[0] = 1  # s[0] is valid (not "0")

        for i in range(1, n):
            # single digit s[i]
            if s[i] != "0":
                dp[i] += dp[i - 1]

            # double digit s[i-1:i+1]
            two = int(s[i - 1:i + 1])
            if 10 <= two <= 26:
                dp[i] += 1 if i == 1 else dp[i - 2]

        return dp[n - 1]