class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        
        nums.sort()
        output = []

        for i in range(n-2):
            val = nums[i]
            l = i + 1
            r = n - 1
            if val > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                if val + nums[l] + nums[r] == 0:
                    output.append([val,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif val + nums[l] + nums[r] > 0:
                    r -= 1
                elif val + nums[l] + nums[r] < 0:
                    l += 1

        return output















        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
        