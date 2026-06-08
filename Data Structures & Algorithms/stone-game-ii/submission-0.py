class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def dfs(i, M):
            if i >= n:
                return 0
            if (i, M) in dp:
                return dp[(i, M)]
            
            best = 0
            for x in range(1, 2 * M + 1):
                # current player takes x piles, opponent plays optimally from i+x
                opponent = dfs(i + x, max(M, x))
                best = max(best, suffix[i] - opponent)
            
            dp[(i, M)] = best
            return best

        return dfs(0, 1)