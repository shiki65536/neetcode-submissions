class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        # dp[i-2], dp[i-1]
        prev2 = 1
        prev1 = 1

        for i in range(1, len(s)):
            curr = 0

            # 1-digit decode is valid if s[i] != '0'
            if s[i] != "0":
                curr += prev1

            # 2-digit decode is valid if 10..26
            two = int(s[i - 1:i + 1])
            if 10 <= two <= 26:
                curr += prev2

            prev2 = prev1
            prev1 = curr

            if prev1 == 0:  # optional early exit
                # still safe to continue, but can return early
                pass

        return prev1