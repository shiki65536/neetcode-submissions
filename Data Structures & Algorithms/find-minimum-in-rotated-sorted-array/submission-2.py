class Solution:
    def findMin(self, nums: List[int]) -> int:
        boundary = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                boundary = l
                return nums[boundary]
            
            mid = (l+r) // 2 
            if nums[l] > nums[mid]:
                boundary = mid
                r = mid
            else: # nums[l] < nums[mid]
                l = mid + 1
        
        return nums[boundary]

















        # l, r = 0, len(nums) - 1

        # while l < r:
        #     mid = (l + r) // 2
        #     if nums[mid] > nums[r]:
        #         l = mid + 1
        #     else:
        #         r = mid
        # return nums[l]