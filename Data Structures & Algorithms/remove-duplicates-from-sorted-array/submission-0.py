class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] == nums [l+1]:
                nums.pop(l+1)
                r -= 1
            else:
                l += 1
        return len(nums)