class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        # # array
        # dp = [0]* (n+1) 
        # dp[1] = 1
        # dp[2] = 1

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]+ dp[i-3]
        # return dp[n]

        # number
        prev1 = 0
        prev2 = 1
        prev3 = 1
        for i in range(3, n+1):
            curr = prev1 + prev2 + prev3
            prev1 = prev2
            prev2 = prev3
            prev3 = curr
        
        return prev3
