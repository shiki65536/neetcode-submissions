class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(n-1):
            for j in range(i+1, n):
                target = -(nums[i] +  nums[j])

                if target in nums:
                    index = nums.index(target)
                    if index != i and index != j:
                        value = sorted([nums[i], nums[j], target])
                        if value not in res:
                            res.append(value)
        
        return list(res)
        