class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        def calculate(start, end):
            prev1 = 0
            prev2 = 0
            for i in range(start, end):
                curr = max(prev1 + nums[i], prev2)
                prev1 = prev2
                prev2 = curr
            return prev2

        with_first = calculate(0, len(nums)-1)
        with_last = calculate(1, len(nums))
        
        return max(with_first, with_last)