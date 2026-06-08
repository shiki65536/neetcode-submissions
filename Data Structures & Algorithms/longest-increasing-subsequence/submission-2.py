class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = []

        memo = [-1] * n
        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            length = 1
            for j in range(i, n):
                if nums[j] > nums[i]:
                    length = max(length, 1 + dfs(j))
            memo[i] = length
            return length
        
        for i in range(n):
            res.append(dfs(i))
        
        return max(res)
