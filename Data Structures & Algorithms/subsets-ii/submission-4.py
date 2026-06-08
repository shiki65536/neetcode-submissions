class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(start, path):
            res.append(path.copy())
            if start == len(nums):
                return   
            for i in range(start, len(nums)):
                if start < i and nums[i-1] == nums[i]:
                    continue 
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res    
