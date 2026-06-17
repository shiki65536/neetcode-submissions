class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        # invariant >  l <= ans <= r
        while l <= r:
            mid = (l+r) // 2
            val = nums[mid]
            left = nums[l]
            right = nums[r]
            if val == target or target == left or target == right:
                return True
            elif left < val:
                if left < target < val:
                    r = mid - 1
                else: # val > target:
                    l = mid + 1
            elif left > val:
                if val < target < right:
                    l = mid + 1
                else: # val > target:
                    r = mid - 1
            else:
                l += 1

        return False















        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l+r) // 2
        #     if nums[mid] == target:
        #         return True
        #     elif nums[l] < nums[mid]:
        #         if nums[l] <= target < nums[mid]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     elif nums[l] > nums[mid]: 
        #         if nums[mid] < target <= nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid -1
        #     else:
        #         l += 1
        
        # return False