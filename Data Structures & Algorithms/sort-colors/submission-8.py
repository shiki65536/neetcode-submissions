class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, pointer, right = 0, 0, n-1

        while pointer <= right:
            if nums[pointer] == 0:
                nums[left], nums[pointer] = nums[pointer], nums[left]
                left += 1
                pointer += 1
            elif nums[pointer] == 2:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                right -= 1
            else:
                pointer += 1













        # start = 0
        # end = len(nums) - 1
        # i = 0
        # n = len(nums) - 1
        # while i <= end:
        #     if nums[i] == 0:
        #         nums[start], nums[i] = nums[i], nums[start]
        #         start += 1
        #         i += 1
        #     elif nums[i] == 2:
        #         nums[end], nums[i] = nums[i], nums[end]
        #         end -= 1
        #     else:
        #         i += 1
        
        # dry run
        # [1,0,2,1] 
        # [1,0,2,1] i=0
        # [0,1,2,1] i=1, start +=1
        # [0,1,2,1] i=1
        # [0,1,1,2] i=2, end -=1


