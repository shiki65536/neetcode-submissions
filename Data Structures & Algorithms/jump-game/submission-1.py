class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        def dfs(i):
            if len(nums) - 1 < i:
                return
            if dp[i]:
                return
            
            dp[i] = True
            for j in range(1, nums[i]+1):
                dfs(i+j)
        
        dfs(0)
        print(dp)
        
        return dp[len(nums)-1]
             