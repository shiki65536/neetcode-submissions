class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)

        res = 0
        total = 0

        for num in nums:
            total += num

            res += seen[total - k] # important to add at first

            if total == k: # self is the answer
                res += 1

            seen[total] += 1 # important: not add first to avoid findign self

        return res