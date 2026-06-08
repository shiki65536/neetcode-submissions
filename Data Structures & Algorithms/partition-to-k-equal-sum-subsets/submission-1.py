class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total//k
        subset = [0] * k
        nums.sort(reverse=True)

        def backtrack(i):
            if i == len(nums):
                for j in range(k):
                    if subset[j] != target:
                        return False
                return True
            for j in range(k):
                if nums[i] + subset[j] <= target:
                    subset[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    subset[j] -= nums[i]
                    if subset[j] == 0:
                        break
            return False
        
        return backtrack(0)