class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = math.inf
        l = 0
        total = 0
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target and l <= r:
                best = min(best, r-l+1)
                total -= nums[l]
                l += 1

        return best if best != math.inf else 0


















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