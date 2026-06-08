class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N

        for i in range(N):
            tmp = nums[i]
            for j in range(i):
                if tmp > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
