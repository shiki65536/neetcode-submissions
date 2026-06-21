class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0, 0
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            if height[l] < height[r]:
                maxL = max(maxL, height[l])
                res += (maxL - height[l])
                l += 1
            else:
                maxR = max(maxR, height[r])
                res += (maxR - height[r])
                r -= 1

        return res








        # l, r = 0, len(height) - 1
        # max_l, max_r = 0, 0
        # res = 0

        # while l < r:
        #     if height[l] < height[r]:
        #         max_l = max(max_l, height[l])
        #         res += max_l - height[l]
        #         l += 1
        #     else:
        #         max_r = max(max_r, height[r])
        #         res += max_r - height[r]
        #         r -= 1

        # return res



        # l, r = 0, len(height) - 1
        # max_l = 0
        # max_r = 0
        # water = 0

        # while l < r:
        #     if height[l] <= height[r]:
        #         if height[l] > max_l:
        #             max_l = height[l]
        #         else:
        #             water += (max_l - height[l])
        #         l += 1
        #     else:
        #         if height[r] > max_r:
        #             max_r = height[r]
        #         else:
        #             water += (max_r - height[r])
        #         r -= 1
        
        # return water

