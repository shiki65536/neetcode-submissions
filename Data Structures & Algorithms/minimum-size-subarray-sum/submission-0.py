class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        n = len(nums)
        best = float("inf")
        total = 0

        while r < n and l <= r:
            total += nums[r]
            while total >= target:
                best = min(best, r-l+1)
                total -= nums[l]
                l+= 1
            r += 1

        return 0 if best == float("inf") else best