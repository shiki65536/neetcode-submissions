class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        spend = [0] * len(cost)
        spend[0] = cost[0]
        spend[1] = cost[1]

        for i in range(2, len(cost)):
            pay = min(cost[i] + spend[i-2], cost[i] + spend[i-1])
            spend[i] = pay

        
        return min(spend[-1], spend[-2])