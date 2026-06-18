class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                best = max(best, prices[r]-prices[l])

        return best














        max_amount = 0
        start = prices[0]

        for price in prices[1:]:
            start = min(start, price)
            max_amount = max(max_amount, price - start)
        
        return max_amount
