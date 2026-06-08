class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair: (index, height)
        max_area = 0 

        for i, h in enumerate(heights + [0]):
            start = i
            while len(stack) > 0 and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index 
                max_area = max(max_area, width * height)
                start = index
            stack.append((start, h))

        return max_area