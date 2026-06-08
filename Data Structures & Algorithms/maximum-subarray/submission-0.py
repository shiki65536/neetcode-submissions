class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        tmp_sum = float("-inf")

        for num in nums:
            tmp_sum = max(tmp_sum + num, num)
            max_sum = max(max_sum, tmp_sum)
        
        return max_sum
