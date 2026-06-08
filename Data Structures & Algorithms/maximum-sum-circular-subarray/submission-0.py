class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best = float("-inf")
        
        for i in range(len(nums)):
            total = float("-inf")
            for j in range(i, len(nums) + i):
                j = j%len(nums)
                total = max(nums[j], total+nums[j])
                best = max(best, total)

        return best
