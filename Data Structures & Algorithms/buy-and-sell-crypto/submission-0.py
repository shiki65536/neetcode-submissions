class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_amount = 0
        start = prices[0]

        for price in prices[1:]:
            start = min(start, price)
            max_amount = max(max_amount, price - start)
        
        return max_amount
