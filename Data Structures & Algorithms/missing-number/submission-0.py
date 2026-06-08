class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        output = len(nums)

        for i in range(len(nums)):
            output ^= i
            output ^= nums[i]

        return output