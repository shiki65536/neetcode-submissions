class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(idx,path):
            if len(idx) == n :
                if path not in res:
                    res.append(path[:])
            if len(idx) >= n:
                return
            for i in range(n):
                if i not in idx:
                    idx.append(i)
                    path.append(nums[i])
                    backtrack(idx, path)
                    idx.pop()
                    path.pop()
        backtrack([],[])
        return res
                
