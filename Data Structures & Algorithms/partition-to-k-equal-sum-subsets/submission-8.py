class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        memo = {} #
        seen = [0] * n
        count = 0

        def backtrack(remain):
            if all(seen) and remain == 0:
                return True
            if remain == 0:
                remain = target
            if tuple(seen) in memo:
               return  memo[tuple(seen)]
            ans = False
            for i in range(n):
                if not seen[i] and remain - nums[i] >= 0:
                    seen[i] = 1
                    if backtrack(remain - nums[i]):
                        memo[tuple(seen)] = True
                        ans = True
                        return ans
                    seen[i] = 0
            memo[tuple(seen)] = ans
            return ans

        return backtrack(target)


















        # total = sum(nums)
        # if total % k != 0:
        #     return False
        
        # target = total//k
        # subset = [0] * k
        # nums.sort(reverse=True)

        # def backtrack(i):
        #     if i == len(nums):
        #         for j in range(k):
        #             if subset[j] != target:
        #                 return False
        #         return True
        #     for j in range(k):
        #         if nums[i] + subset[j] <= target:
        #             subset[j] += nums[i]
        #             if backtrack(i+1):
        #                 return True
        #             subset[j] -= nums[i]
        #             if subset[j] == 0:
        #                 break
        #     return False
        
        # return backtrack(0)