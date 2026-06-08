class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(start, remain):
            if remain == 0:
                res.append(path[:])
                return 
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                if candidates[i] > remain:
                    break
                    
                path.append(candidates[i])
                backtrack(i+1, remain - candidates[i])
                path.pop()
        
        backtrack(0, target)
        return res