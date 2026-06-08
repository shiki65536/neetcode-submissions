class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        n = len(nums) 
        
        def backtrack(path):
            if len(path) == n :
                res.append(path[:])
            if len(path) >= n:
                return
            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path)
                    used[i] = False
                    path.pop()
        backtrack([])
        return res
                
