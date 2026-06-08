from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True)
        best = float("inf")

        def dfs(idx: int, remain: int, used: int) -> None:
            nonlocal best
            if remain == 0:
                best = min(best, used)
                return
            if idx == len(coins):
                return

            coin = coins[idx]

            # 最多可以用幾枚這個 coin
            max_take = remain // coin

            # 從多拿到少拿（更容易早找到短解）
            for k in range(max_take, -1, -1):
                new_used = used + k
                if new_used >= best:
                    continue

                new_remain = remain - k * coin
                if new_remain == 0:
                    best = min(best, new_used)
                    return

                # 下界剪枝：即使之後都用下一種最大 coin，也至少要這麼多枚
                if idx + 1 < len(coins):
                    next_coin = coins[idx + 1]
                    lower_bound = (new_remain + next_coin - 1) // next_coin
                    if new_used + lower_bound >= best:
                        continue

                dfs(idx + 1, new_remain, new_used)

        dfs(0, amount, 0)
        return -1 if best == float("inf") else best