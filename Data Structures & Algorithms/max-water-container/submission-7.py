class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxi = float("-inf")

        while l < r :
            width = r - l
            height = min(heights[l], heights[r])
            maxi = max(maxi, width*height)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxi