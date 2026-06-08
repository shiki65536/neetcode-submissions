class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin = nums[0]
        curMax = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                curMin, curMax = curMax, curMin
            curMax = max(curMax * nums[i], nums[i])
            curMin = min(curMin * nums[i], nums[i])
            res = max(res, curMax)
        return res