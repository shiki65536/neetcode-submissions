class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start+1, n+1):
                path.append(i)
                backtrack(i, path)
                path.pop()
        backtrack(0, [])

        return res
