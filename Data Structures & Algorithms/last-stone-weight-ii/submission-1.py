class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = (sum(stones) + 1) // 2
        dp = {}
        
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (sum(stones)-total))
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total+stones[i]))
            return dp[(i,total)]

        return dfs(0,0)
        # n = len(stones)
        # if n == 1:
        #     return stones[0]

        # dp = [0] * (n+1)

        # for i in range(n):
        #     d_i = i + 1
        #     curr_mass = stones[i]
        #     dp[d_i] = abs(dp[d_i-1] - curr_mass)

        # return dp[n]