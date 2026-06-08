class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(start, remain):
            if remain == 0:
                if path[:] not in res:
                    res.append(path[:])
                return 
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i+1, remain - candidates[i])
                path.pop()
        
        backtrack(0, target)
        return res