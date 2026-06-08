class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not isinstance(nums, list):
            raise TypeError("nums must be a list")
        if not all(isinstance(x, int) for x in nums):
            raise TypeError("nums must be a list of integers")
        if not isinstance(target, int):
            raise TypeError("target must be an integer")

        seen = {}
        for i, num in enumerate(nums):
            gap = target - num
            if gap in seen:
                return [seen[gap], i]
            else:
                seen[num] = i
        return [-1]
