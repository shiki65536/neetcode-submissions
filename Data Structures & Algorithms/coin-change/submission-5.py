from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort()
        best = float("inf")

        def backtrack(start: int, remain: int, used: int) -> None:
            nonlocal best

            if remain == 0:
                best = min(best, used)
                return

            if used >= best:
                return

            for i in range(start, len(coins)):
                c = coins[i]
                if c > remain:
                    break  # 後面更大，直接停

                backtrack(i, remain - c, used + 1)  # i 代表可以重複用同一硬幣

        backtrack(0, amount, 0)
        return -1 if best == float("inf") else best