class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        temp = []

        for r, num in enumerate(nums):
            temp.append(num)
            if len(temp) == k:
                res.append(max(temp))
                temp.pop(0)
        
        return res

