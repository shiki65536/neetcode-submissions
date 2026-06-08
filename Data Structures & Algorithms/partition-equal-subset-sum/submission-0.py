class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # edge
        if sum(nums) % 2 != 0:
            return False
        if len(nums) == 1:
            return False
        
        def backtrack(start, remain):
            if remain == 0:
                return True
            if remain < 0:
                return False
            
            for i in range(start+1, len(nums)):
                remain -= nums[i]
                if backtrack(i, remain):
                    return True
                remain += nums[i]
            return False
        
        for i in range(len(nums)):
            if backtrack(i, sum(nums)//2):
                return True
        
        return False
            